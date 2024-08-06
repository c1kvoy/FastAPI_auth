from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from ..schemas.methods import *
from ..schemas.schemas import *
from ..models.models import *
from sqlalchemy.ext.asyncio import AsyncSession
from src.app.db import *
from .hash_utils import *

auth_router = APIRouter(prefix="/auth", tags=["auth"])

oauth2 = OAuth2PasswordBearer(tokenUrl="auth/token")


async def validate_user(form: OAuth2PasswordRequestForm = Depends(),
                        dbs: AsyncSession = Depends(get_async_session)) -> UserOutSchema:
    query = select(User).where(User.username == form.username)
    result = await dbs.execute(query)
    user = result.scalar()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    print(form.password.encode())
    print(user.hashed_password.encode())
    if not verify_password(form.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect password")
    print(user)
    return user


@auth_router.post("/token")
async def login(user: UserOutSchema = Depends(validate_user)):
    jwt_payload = {
        "sub": user.id,
        "username": user.username,
        "email": user.email,
    }
    print(jwt_payload)
    token = encode_jwt(jwt_payload)
    print(token)
    return TokenInfo(access_token=token, token_type="Bearer")

# @auth_router.get("/gets")
# async def auth_test(token:str = Depends(oauth2)):
#     return {"Okey": "Good"}
