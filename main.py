from typing import Annotated

from fastapi import FastAPI, Depends
# Talvin, Alex

from Auth.auth import auth_router, det_current_user
from Root.root import root_router
from Single.single import single_router
from Admin.admin import admin_router

from Models import models
from database.database import engine


app = FastAPI(
    title="PixiePlace"
)

models.Base.metadata.create_all(bind=engine)
app.include_router(auth_router)
app.include_router(root_router)
app.include_router(single_router)
app.include_router(admin_router)



