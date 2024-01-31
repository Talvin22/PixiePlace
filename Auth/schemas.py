from typing import Optional

from pydantic import BaseModel
from fastapi_users import schemas


# class CreateUserRequest(BaseModel):
#     username: str
#     email: str
#     first_name: str
#     last_name: str
#     password: str
#     role: str
#     phone_number: str
#
#
# class Token(BaseModel):
#     access_token: str
#     token_type: str
#
#
# class User(BaseModel):
#     email: str
#     phone_number: str
#     username: str
#     first_name: str
#     last_name: str
#     hashed_password: str
#     role: str


class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    username: str
    first_name: str
    role: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False


class UserCreate(schemas.BaseUserCreate):
    username: str
    first_name: str
    last_name: str
    password: str
    role: str
    phone_number: str
    email: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserUpdate(schemas.BaseUserUpdate):
    pass
