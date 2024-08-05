from ..schemas.schemas import *
from ..schemas.methods import *
from ..models.models import *
from fastapi import APIRouter, Depends, HTTPException
from src.app import db
user_router = APIRouter(tags=["user"])


@user_router.on_event("startup")
async def on_startup():
    await db.create_tables()


@user_router.put("/user/create")
async def create_user_endpoint(user: UserInSchema, db=Depends(db.get_async_session)):
    user_db = await create_user(user, db)
    return user_db


@user_router.get("/user/get")
async def get_user_endpoint(db=Depends(db.get_async_session)):
    users = await get_all_users(db)
    return users
