from fastapi import HTTPException, status
from ..auth.hash_utils import *
from .schemas import *
from sqlalchemy.ext.asyncio import AsyncSession
from ..models.models import *
from sqlalchemy.future import select
from fastapi.security import HTTPBasicCredentials


async def create_user(user_in: UserInSchema, db: AsyncSession):
    user = user_in.dict()
    user["hashed_password"] = hash_password(user_in.hashed_password).decode()
    user = User(**user)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


async def get_all_users(db: AsyncSession):
    users = select(User)
    users = await db.execute(users)
    result = users.scalars().all()
    return result




# async def user_auth(db: AsyncSession, credentials: HTTPBasicCredentials):
#     query = select(User).where(User.username == credentials.username)
#     user = await db.execute(query)
#     result = user.scalars().first()
#     if not result:
#         raise  HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Invalid username or password",
#         headers={"WWW-Authenticate": "Basic"},
#     )
#     else:
#         if credentials.password != result.hashed_password:
#             HTTPException(
#                 status_code=status.HTTP_401_UNAUTHORIZED,
#                 detail="Invalid username or password",
#                 headers={"WWW-Authenticate": "Basic"},
#             )
#         else:
#             return result
