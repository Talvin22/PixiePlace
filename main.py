from fastapi import FastAPI

from Auth.auth import auth_router
from Models import models
from database.database import engine

app = FastAPI(
    title="PixiePlace"
)
models.Base.metadata.create_all(bind=engine)
app.include_router(auth_router)
