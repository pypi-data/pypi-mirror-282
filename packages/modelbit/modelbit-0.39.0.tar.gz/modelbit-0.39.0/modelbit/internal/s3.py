#!/usr/bin/env python3
import base64
import os
import logging
from typing import cast, List, Optional
from modelbit.utils import tempFilePath
from .encryption import decryptAndValidateToFile

logger = logging.getLogger(__name__)


def getS3FileBytes(keySuffix: str):
  with tempFilePath() as tmpPath:
    _downloadDecrypt(s3Key=f"{_workspaceId()}/{keySuffix}", storePath=tmpPath)
    with open(tmpPath, "rb") as f:
      return f.read()


def getRuntimeObjectToBytes(contentHash: str) -> bytes:
  getRuntimeObjectToFile(contentHash)
  with open(s3ObjectCachePath(contentHash=contentHash), "rb") as f:
    return f.read()


def getRuntimeObjectToFile(contentHash: str) -> None:
  cachePath = s3ObjectCachePath(contentHash=contentHash)
  try:
    return _downloadDecryptRuntimeObject(cachePath=cachePath, contentHash=contentHash, skipIfExists=True)
  except Exception as err:
    logger.info("Failed to read from cache", exc_info=err)
    return _downloadDecryptRuntimeObject(cachePath=cachePath, contentHash=contentHash, skipIfExists=False)


def _workspaceId() -> str:
  return os.environ['WORKSPACE_ID']


def _pystateBucket() -> str:
  return os.environ['PYSTATE_BUCKET']


def _pystateKeys() -> List[str]:
  return os.environ['PYSTATE_KEYS'].split(",")


def s3ObjectCachePath(contentHash: str) -> str:
  tempDir = os.getenv("MB_TEMP_DIR_OVERRIDE", "/tmp/modelbit")
  rtDir = "/runtime_objects" if os.path.exists("/runtime_objects") else f"{tempDir}/runtime_objects"
  return os.path.join(rtDir, contentHash + ".zstd.enc")


# We store the decrypted version in deployment's cache
def _downloadDecryptRuntimeObject(cachePath: str, contentHash: str, skipIfExists: bool = False) -> None:

  return _downloadDecrypt(s3Key=f'{_workspaceId()}/runtime_objects/{contentHash}.zstd.enc',
                          storePath=cachePath,
                          contentHash=contentHash,
                          skipIfExists=skipIfExists)


def _downloadDecrypt(s3Key: str,
                     storePath: str,
                     contentHash: Optional[str] = None,
                     skipIfExists: bool = False) -> None:
  from Cryptodome.Cipher import AES
  from Cryptodome.Util.Padding import unpad
  from modelbit.utils import boto3Client

  if skipIfExists and os.path.exists(storePath):
    return

  s3Client = boto3Client("s3")
  s3Obj = s3Client.head_object(Bucket=_pystateBucket(), Key=s3Key)
  fileKeyEnc = base64.b64decode(cast(str, s3Obj['Metadata']["x-amz-key"]))
  fileIv = base64.b64decode(cast(str, s3Obj['Metadata']["x-amz-iv"]))
  lastError = None

  for key64 in _pystateKeys():
    try:
      cipher = AES.new(base64.b64decode(key64), AES.MODE_ECB)  # type: ignore
      fileKey = unpad(cipher.decrypt(fileKeyEnc), AES.block_size)
      cipher = AES.new(fileKey, AES.MODE_CBC, fileIv)  # type: ignore

      with tempFilePath() as encFilePath:
        logger.info(f"Downloading {s3Key}")
        with open(encFilePath, "wb") as fileObj:
          s3Client.download_fileobj(Bucket=_pystateBucket(), Key=s3Key, Fileobj=fileObj)

        logger.info(f"Decrypting {s3Key}")
        return decryptAndValidateToFile(encFilePath=encFilePath,
                                        key64=base64.b64encode(fileKey).decode(),
                                        iv64=base64.b64encode(fileIv).decode(),
                                        toFile=storePath,
                                        desc=s3Key,
                                        expectedHash=contentHash)
    except MemoryError as err:
      raise err
    except Exception as err:
      logger.exception(f"DecryptionFailure: {err}\n")
      import traceback
      print(f"DecryptionFailure: {err}\n", traceback.format_exc())
      lastError = err
      pass
  raise Exception(f"Unable to decrypt: {str(lastError)}")
