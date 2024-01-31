from fastapi_users import fastapi_users, FastAPIUsers
from fastapi import FastAPI

from Auth.auth import auth_backend
from Auth.database import User
from Auth.manager import get_user_manager
from Auth.schemas import UserRead, UserCreate
# from Root.root import root_router
# from Single.single import single_router
# from Admin.admin import admin_router

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app = FastAPI(
    title="PixiePlace"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

# app.include_router(root_router)
# app.include_router(single_router)
# app.include_router(admin_router)
