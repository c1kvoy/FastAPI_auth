from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from ..schemas.methods import *
from sqlalchemy.ext.asyncio import AsyncSession
from src.app.db import *

auth_router = APIRouter()

security = HTTPBasic()


@auth_router.post("/basic_auth")
async def basic_auth(credentials: HTTPBasicCredentials = Depends(security), db=Depends(db.get_async_session)):
    user_db = await user_auth(db, credentials)
    return user_db
