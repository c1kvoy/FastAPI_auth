from fastapi import FastAPI
from src.app.api.routers.user_router import user_router
from src.app.api.auth.auth_router import auth_router

app = FastAPI()
app.include_router(user_router)
app.include_router(auth_router)