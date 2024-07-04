import codecs
from datetime import datetime, timedelta
import json
import logging
import os
import sys
from typing import Any, Dict, List, Optional, Tuple, Union, TextIO, cast
from tqdm import tqdm
from io import StringIO
from concurrent.futures import ThreadPoolExecutor

from modelbit.api import MbApi, BranchApi, RegistryApi
from modelbit.error import UserFacingError
from modelbit.helpers import getCurrentBranch
from modelbit.internal.auth import isAuthenticated as isAuthenticated
from modelbit.internal.describe import calcHash, describeObject
from modelbit.internal.retry import retry
from modelbit.internal.runtime_objects import downloadRuntimeObject, uploadRuntimeObject
from modelbit.internal.s3 import getS3FileBytes
from modelbit.internal.secure_storage import DownloadableObjectInfo, getSecureData
from modelbit.utils import inDeployment, maybePlural, tryPickle, tryUnpickle, dumpJson, getSerializerDesc
from modelbit.ux import printTemplate
from modelbit.keras_wrapper import KerasWrapper
from modelbit.internal import tracing

logger = logging.getLogger(__name__)

_reg_cache: Optional[Tuple[datetime, str]] = None
_obj_cache: Dict[str, Any] = {}

_usedModelsByFunction: Dict[str, List[Any]] = {}  # function name to list of models
_usedSerializers: Dict[str, None] = {}

MaxJsonRequestSize = 5_000_000


def registryCacheTtl():
  if inDeployment():
    return timedelta(seconds=60)
  return timedelta(seconds=10)


def set(api: MbApi,
        name: str,
        model: Any,
        metrics: Optional[Dict[str, Any]] = None,
        serializer: Optional[str] = None):
  BranchApi(api).raiseIfProtected()
  _assertSetModelFormat(name=name, model=model, metrics=metrics)
  _assertSerializer(serializer=serializer)
  set_many(api, models={name: model}, metrics={name: metrics}, serializer=serializer)


def set_many(api: MbApi,
             models: Dict[str, Any],
             metrics: Optional[Dict[str, Optional[Dict[str, Any]]]] = None,
             serializer: Optional[str] = None):
  BranchApi(api).raiseIfProtected()
  _assertSetModelsFormat(models=models, metrics=metrics)
  _assertSerializer(serializer=serializer)

  _uploadModelFromNotebook(api, models=models, metrics=metrics, serializer=serializer)
  printTemplate(
      "message",
      None,
      msgText=f"Success: {len(models)} {maybePlural(len(models), 'model')} added to the registry.",
  )


def _uploadModelFromNotebook(api: MbApi,
                             models: Dict[str, Any],
                             metrics: Optional[Dict[str, Any]],
                             batchSize: int = 100,
                             serializer: Optional[str] = None):
  perFileLoader = len(models) < 10
  uploadedObjects: Dict[str, Any] = {}
  uploadedObjectBatches = [uploadedObjects]
  outputStream: TextIO = StringIO() if os.getenv('MB_TXT_MODE') else sys.stdout
  readyMetrics: Dict[str, Any] = metrics if metrics else {}

  if perFileLoader:
    for name, obj in models.items():
      uploadedObjects[name] = _pickleAndUpload(api=api,
                                               name=name,
                                               obj=obj,
                                               showLoader=True,
                                               metrics=readyMetrics.get(name),
                                               serializer=serializer)
  else:
    for name, obj in tqdm(models.items(),
                          desc=f"Uploading {len(models)} models",
                          bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} models [{elapsed}<{remaining}]",
                          file=outputStream):
      if len(uploadedObjects) >= batchSize or len(json.dumps(uploadedObjects)) > MaxJsonRequestSize / 2:
        uploadedObjects = {}
        uploadedObjectBatches.append(uploadedObjects)
      uploadedObjects[name] = _pickleAndUpload(api=api,
                                               name=name,
                                               obj=obj,
                                               showLoader=False,
                                               metrics=readyMetrics.get(name),
                                               serializer=serializer)

  for uploadedObjects in tqdm(uploadedObjectBatches,
                              desc=f"Updating registry",
                              bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]",
                              file=outputStream):
    _assertSetModelsRequestSize(uploadedObjects)
    RegistryApi(api).storeContentHashAndMetadata(uploadedObjects)


def set_metrics(api: MbApi, name: str, metrics: Dict[str, Any], merge: bool = False):
  BranchApi(api).raiseIfProtected()
  _assertSetModelMetricsFormat({name: metrics}, [name])
  RegistryApi(api).updateMetadata(name, metrics, merge)
  printTemplate("metrics-updated", None, name=name)


def get(api: MbApi, name: str):
  _assertGetFormat(name)

  if (inDeployment() and name in _obj_cache):
    obj = _obj_cache[name]
    _logModelUsed(name, obj)
    return obj

  reg = _getRegistry(api)
  if reg is None:
    raise UserFacingError(f"Model not found: {name}")

  for line in reg.split("\n"):
    if line.startswith(f"{name}="):
      jsonStr = line[len(name) + 1:]
      hash, serializerPackage = _tryReadHash(jsonStr)
      if hash:
        serializer = serializerPackage.split("==")[0] if type(serializerPackage) is str else None
        obj = _getObject(api=api, name=name, contentHash=hash, serializer=serializer)
        _logModelUsed(name=name, model=obj, serializer=serializer)
        return obj
  raise UserFacingError(f"Model not found: {name}")


def getMany(api: MbApi, prefix: Optional[str], names: Optional[List[str]]) -> Dict[str, Any]:
  _assertGetManyFormat(prefix=prefix, names=names)

  if names is None:
    names = list_names(api, prefix)

  results: Dict[str, Any] = {}
  if len(names) == 0:
    return results
  _getRegistry(api)  # load registry once before threads start up

  def getOne(name: str):
    with tracing.trace(name, False):
      results[name] = get(api, name)

  with ThreadPoolExecutor(max_workers=4) as executor:
    for name in names:
      executor.submit(getOne, name)
    executor.shutdown(wait=True)
  return results


def getMetrics(api: MbApi, nameOrNames: Union[str, List[str]]) -> Optional[Dict[str, Any]]:
  if type(nameOrNames) is str:
    metrics = RegistryApi(api).fetchModelMetrics([nameOrNames])
    return metrics.get(nameOrNames, None)
  elif type(nameOrNames) is list:
    for n in nameOrNames:
      if type(n) is not str:
        raise UserFacingError(f"Model names must be strings. Found {n} which is a {type(n)}.")
      if n == "":
        raise UserFacingError(f"Model names cannot be empty strings.")
    if len(nameOrNames) == 0:
      raise UserFacingError(f"Supply at least one model name to fetch metrics.")
    return RegistryApi(api).fetchModelMetrics(nameOrNames)
  else:
    raise UserFacingError(f"Error getting metrics. Expecting str or List[str] but found {type(nameOrNames)}")


def _logModelUsed(name: str, model: Any, serializer: Optional[str] = None):
  if inDeployment():
    print(f'![mb:model]({name})')  # for parsing out of stdout later
  else:
    import traceback
    foundGetModel = False
    frame = traceback.extract_stack()
    frame.reverse()
    for f in frame:
      if not foundGetModel:  # first, look for get_model in stack
        if f.name == "get_model":
          foundGetModel = True
        continue
      if f.filename.endswith("modelbit/telemetry.py"):  # then skip over internal wrappers
        continue
      if f.name not in _usedModelsByFunction:  # finally, capture name of function that called get_model
        _usedModelsByFunction[f.name] = []
      if model not in _usedModelsByFunction[f.name]:
        _usedModelsByFunction[f.name].append(model)
      if serializer is not None:
        _usedSerializers[serializer] = None
      return


def recentlyUsedModels(funcName: str) -> List[Any]:
  return _usedModelsByFunction.get(funcName, []).copy()


def recentlyUsedSerializers() -> List[str]:
  return list(_usedSerializers.keys())


def resetRecentlyUsedModels():
  _usedModelsByFunction.clear()
  _usedSerializers.clear()


def list_names(api: MbApi, prefix: Optional[str] = None):
  _assertListFormat(prefix)

  reg = _getRegistry(api)
  if reg is None:
    return cast(List[str], [])

  if prefix is not None:
    return [line[0:line.index("=")] for line in reg.split("\n") if line.startswith(prefix)]
  else:
    return [line[0:line.index("=")] for line in reg.split("\n")]


def delete(api: MbApi, names: Union[str, List[str]]):
  BranchApi(api).raiseIfProtected()
  _assertDeleteFormat(names)
  if not isinstance(names, List):
    names = [names]

  RegistryApi(api).delete(names)
  printTemplate(
      "message",
      None,
      msgText=f"Success: {len(names)} {maybePlural(len(names), 'model')} removed from the registry.",
  )


def _assertSetModelFormat(name: str, model: Any, metrics: Optional[Dict[str, Any]]):
  if type(name) is not str:
    raise UserFacingError(f"name= must be a string. It's currently a {type(name)}")
  if not name:
    raise UserFacingError(f"name= must not be empty.")
  if len(name) < 2:
    raise UserFacingError(f"Model names must be at least two characters.")
  if model is None:
    raise UserFacingError(f"model= must not be None.")
  _assertSetModelMetricsFormat({name: metrics}, [name])


def _assertSetModelsFormat(models: Dict[str, Any], metrics: Optional[Dict[str, Any]]):
  if type(models) is not dict:
    raise UserFacingError(f"models= must be a dictionary. It's currently a {type(models)}")
  if len(models) == 0:
    raise UserFacingError(f"The dict of models to add cannot be empty.")
  for k, v in models.items():
    if type(k) is not str:
      raise UserFacingError(f"Model keys must be strings. Found '{k}' which is a {type(v)}")
    if not k:
      raise UserFacingError(f"Model keys must not be empty.")
    if v is None:
      raise UserFacingError(f"Model values must not be None.")
    if len(k) < 2:
      raise UserFacingError(f"Model keys must be at least two characters.")
  _assertSetModelMetricsFormat(metrics, list(models.keys()))


def _assertSetModelMetricsFormat(metrics: Optional[Dict[str, Optional[Dict[str, Any]]]],
                                 modelNames: List[str]):
  if metrics is None:
    return
  if type(metrics) is not dict:
    raise UserFacingError(f"Model metrics must be a dictionary of modelName -> metricsDict.")

  for modelName, metricsDict in metrics.items():
    if type(modelName) is not str:
      raise UserFacingError(f"Expecting a string model name as the key, but found {type(modelName)}")
    if metricsDict is None:
      continue
    if type(metricsDict) is not dict:
      raise UserFacingError(f"Expecting a dictionary for metric values, but found {type(metricsDict)}")
    if modelName not in modelNames:
      raise UserFacingError(
          f"Model metrics must be a dictionary of modelName -> metricsDict. There is no model named '{modelName}' in this update."
      )

    for k, v in metricsDict.items():
      if type(k) is not str:
        raise UserFacingError(f"Metric keys must be strings. Found '{k}' which is a {type(k)}")
      if len(k) == 0:
        raise UserFacingError(f"Metric keys cannot be empty strings")
      try:
        dumpJson(v)
      except Exception as err:
        raise UserFacingError(
            f"Metric values must be JSON-serializable. The value of '{k}' is {type(v)}. Error: {err}")


def _assertSerializer(serializer: Optional[str]):
  if serializer not in [None, "cloudpickle"]:
    raise UserFacingError("The 'serializer' value is invalid. It must either be None or 'cloudpickle'.")


def _assertSetModelsRequestSize(request: Dict[str, Any]):
  if len(dumpJson(request)) > MaxJsonRequestSize:
    raise UserFacingError("Request size exceeds maximum allowed (5MB). Add fewer models at a time.")


def _assertDeleteFormat(names: Union[str, List[str]]):
  if type(names) is str:
    if not names:
      raise UserFacingError(f"names= must not be empty.")
    return
  if type(names) is list:
    if not names:
      raise UserFacingError(f"names= must not be empty.")
    for n in names:
      if type(n) is not str:
        raise UserFacingError(f"Names must only contain strings. Found '{n}' which is a {type(n)}")
      if not n:
        raise UserFacingError(f"Names must not contain empty strings")
    return
  raise UserFacingError(f"names= must be a string or a list of strings. It's currently a {type(names)}")


def _assertGetFormat(name: str):
  if type(name) is not str:
    raise UserFacingError(f"name= must be a string. It's currently a {type(name)}")
  if not name:
    raise UserFacingError(f"name= must not be empty.")


def _assertGetManyFormat(prefix: Optional[str], names: Optional[List[str]]):
  if prefix and type(prefix) is not str and (names is None or type(names) is not list or len(names) == 0):
    raise UserFacingError(f"prefix= must be a string or names= must be a list of strings.")
  if prefix and names:
    raise UserFacingError(f"Only one of prefix= or names= can be supplied.")
  if prefix and type(prefix) is not str and not names:
    raise UserFacingError(f"prefix= must be a string. It's currently a {type(prefix)}.")
  if names and type(names) is not list:
    raise UserFacingError(f"names= must be a list of strings.")
  if names:
    for n in names:
      if type(n) is not str:
        raise UserFacingError(f"In the list of names one is not a string: {n}")


def _assertListFormat(prefix: Optional[str]):
  if prefix is None:
    return
  if type(prefix) is not str:
    raise UserFacingError(f"prefix= must be a string. It's currently a {type(prefix)}")
  if not prefix:
    raise UserFacingError(f"prefix= must not be empty.")


def _pickleAndUpload(api: MbApi,
                     name: str,
                     obj: Any,
                     showLoader: bool,
                     metrics: Optional[Dict[str, Any]],
                     serializer: Optional[str] = None):
  objData = tryPickle(obj=_maybeWrap(obj), name=name, serializer=serializer)

  contentHash = calcHash(objData)
  description = describeObject(obj, 1)
  size = len(objData)
  uploadRuntimeObject(api, objData, contentHash, name, showLoader)
  metadata: Dict[str, Any] = {
      "contentHash": contentHash,
      "metadata": {
          "size": size,
          "description": description,
          "trainingJobId": os.environ.get("JOB_ID", None),
          "metrics": metrics,
          "serializer": getSerializerDesc(serializer)
      },
  }
  return metadata


def _getRegistry(api: MbApi) -> Optional[str]:
  global _reg_cache
  if _reg_cache:
    ts, reg = _reg_cache
    if datetime.now() - ts < registryCacheTtl():
      return reg
    else:
      _reg_cache = None

  reg = _getRegistryInDeployment() if inDeployment() else _getRegistryInNotebook(api)
  if reg:
    _reg_cache = datetime.now(), reg
  return reg


def _getRegistryInDeployment():
  registryBytes = _getS3RegistryBytes()
  if registryBytes:
    reg = registryBytes.decode("utf-8")
    return reg


def _getS3RegistryBytes():
  regPath = f"registry_by_branch/{getCurrentBranch()}/registry.txt.zstd.enc"
  return _wrappedGetS3FileBytes(regPath)


def _getRegistryInNotebook(api: MbApi):
  dri = RegistryApi(api).getRegistryDownloadInfo()
  if dri:
    return codecs.decode(_wrappedGetSecureData(dri, "model registry"))


def _tryReadHash(jsonStr: str) -> Tuple[Optional[str], Optional[str]]:  # [hash, serializer]
  try:
    jRes = json.loads(jsonStr)
    hash = jRes.get("id", None)
    serializerPackage = jRes.get("serializer", None)
    if type(hash) is str:
      return (hash, serializerPackage)
    return (None, None)
  except json.JSONDecodeError:
    raise UserFacingError("Unable to find model in registry.")


def _getObject(api: MbApi, name: str, contentHash: str, serializer: Optional[str] = None):
  if contentHash in _obj_cache:
    return _obj_cache[contentHash]

  if inDeployment():
    obj = _getObjectInDeployment(name=name, contentHash=contentHash, serializer=serializer)
  else:
    obj = _getObjectInNotebook(api=api, name=name, contentHash=contentHash, serializer=serializer)
  _obj_cache[contentHash] = obj
  return obj


def _getObjectInDeployment(name: str, contentHash: str, serializer: Optional[str] = None):
  runtimeObjBytes = _getS3ObjectBytes(contentHash)
  assert runtimeObjBytes is not None
  try:
    return _maybeUnwrap(tryUnpickle(obj=runtimeObjBytes, name=name, serializer=serializer))
  except UserFacingError as e:
    raise e
  except ModuleNotFoundError as err:
    raise UserFacingError(f"Module missing from environment: {str(err.name)}")
  except Exception as err:
    raise UserFacingError(f"{err.__class__.__name__} while loading model {name}: {err}")


def _getS3ObjectBytes(contentHash: str):
  return _wrappedGetS3FileBytes(f"runtime_objects/{contentHash}.zstd.enc")


def _getObjectInNotebook(api: MbApi, name: str, contentHash: str, serializer: Optional[str] = None):
  try:
    obj = downloadRuntimeObject(api, contentHash, name)
    return _maybeUnwrap(tryUnpickle(obj=obj, name=name, serializer=serializer))
  except UserFacingError as e:
    raise e
  except ModuleNotFoundError as err:
    raise UserFacingError(f"Module missing from environment: {str(err.name)}")
  except Exception as err:
    raise UserFacingError(f"{err.__class__.__name__} while loading model {name}: {err}")


def _maybeWrap(model: Any):
  if KerasWrapper.isKerasModel(model):
    return KerasWrapper(model)
  return model


def _maybeUnwrap(obj: Any):
  if isinstance(obj, KerasWrapper):
    return obj.getModel()
  return obj


@retry(4, logger)
def _wrappedGetS3FileBytes(path: str):
  return getS3FileBytes(path)


@retry(4, logger)
def _wrappedGetSecureData(dri: DownloadableObjectInfo, desc: str):
  return getSecureData(dri, desc)
