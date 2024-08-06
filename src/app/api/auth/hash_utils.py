import bcrypt
from datetime import datetime, timedelta
from src.app.core.config import settings
import jwt


def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    pwd: bytes = password.encode()
    return bcrypt.hashpw(pwd, salt)


import bcrypt

def verify_password(plain_password: str, hashed_password_in: str) -> bool:
    return bcrypt.checkpw(password=plain_password.encode(), hashed_password=hashed_password_in.encode())

def encode_jwt(payload: dict,
               private_key: str = settings.auth.private_key_path.read_text(),
               ) -> str:
    to_encode = payload.copy()
    now = datetime.utcnow()
    expire = now + timedelta(minutes=15)
    to_encode['exp'] = expire
    encoded = jwt.encode(to_encode, private_key, algorithm='RS256')
    return encoded


def decode_jwt(token: str, public_key: str = settings.auth.public_key_path.read_text()) -> dict:
    decoded = jwt.decode(token, public_key, algorithms=['RS256'])
    return decoded


