from fastapi import Request, Depends
from datetime import datetime, timezone
from jose import jwt, JWTError

from app.config import settings
from app.users.dao import UsersDAO
from app.users.models import Users
from app.exceptions import IncorrectTokenFormatException, TokenAbsentException, TokenExpireException, UserIsNotPresentException

def get_token(request: Request):
    token = request.cookies.get('booking_access_token')
    if not token:
        raise TokenAbsentException
    return token

async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token,
            settings.KEY_JWT,
            settings.ALGORITHM_JWT
        )
    except JWTError:
        raise IncorrectTokenFormatException
    expire: str = payload.get('exp')
    if (not expire) or (int(expire) < datetime.now(timezone.utc).timestamp()):
        raise TokenExpireException
    user_id: str = payload.get('sub')
    if not user_id:
        raise UserIsNotPresentException
    user = await UsersDAO.find_by_id(int(user_id))
    if not user:
        raise UserIsNotPresentException
    return user

async def get_current_admin_user(users: Users = Depends(get_current_user)):
    return users