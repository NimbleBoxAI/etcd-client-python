import pickle
import base64
from typing import Any, Union


def encode(obj: Union[bytes, str]) -> str:
    if type(obj) == type(bytes()):
        return base64.b64encode(obj).decode()
    else:
        return base64.b64encode(obj.encode()).decode()


def decode(b64_str: str) -> bytes:
    return base64.b64decode(b64_str)
