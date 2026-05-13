from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
import jwt
from pydantic import EmailStr
from app.users.dao import UsersDAO
from app.config import settings


ph = CryptContext(schemes=["argon2"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return ph.hash(password)

def verify_password(plain_password, hash_password) -> bool:
    return ph.verify(plain_password, hash_password)

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.KEY_JWT, settings.ALGORITHM_JWT
    )
    return encoded_jwt

async def authentificate_user(email: EmailStr, password: str):
    user = await UsersDAO.find_one_or_none(email=email)
    if user and verify_password(password, user.hashed_password):
        return user

