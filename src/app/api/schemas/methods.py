from fastapi import HTTPException, status

from .schemas import *
from sqlalchemy.ext.asyncio import AsyncSession
from ..models.models import *
from sqlalchemy.future import select
from fastapi.security import HTTPBasicCredentials


async def create_user(user: UserInSchema, db: AsyncSession):
    user = User(**user.dict())
    db.add(user)
    await db.commit()
    await db.refresh(user)
    print(user)
    return user


async def get_all_users(db: AsyncSession):
    users = select(User)
    users = await db.execute(users)
    result = users.scalars().all()
    return result


async def user_auth(db: AsyncSession, credentials: HTTPBasicCredentials):
    query = select(User).where(User.username == credentials.username)
    user = await db.execute(query)
    result = user.scalars().first()
    if not result:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    else:
        if credentials.password != result.hashed_password:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        else:
            return result
