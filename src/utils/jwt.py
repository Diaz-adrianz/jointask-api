from time import time
from jose import jwt

from config import config


def encode(user_id: str):
    payload = {
        "sub": user_id,
        "exp": int(time()) + 15 * 60,
    }

    return jwt.encode(payload, str(config["SECRET_KEY"]), algorithm="HS256")


def decode(token: str) -> dict:
    try:
        payload = jwt.decode(token, str(config["SECRET_KEY"]), algorithms="HS256")
        if "sub" and "exp" not in payload:
            raise Exception
    except:
        raise Exception

    return payload
