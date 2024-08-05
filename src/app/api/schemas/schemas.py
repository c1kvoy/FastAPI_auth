from pydantic import BaseModel


class UserInSchema(BaseModel):
    username: str
    email: str
    hashed_password: str


class UserOutSchema(BaseModel):
    id: int
    username: str
    email: str


class UserInDBSchema(BaseModel):
    id: int
    username: str
    email: str
    hashed_password: str