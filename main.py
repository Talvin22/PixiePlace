from fastapi import FastAPI
# Talvin, Alex
from Auth.auth import auth_router
from Root.root import root_router
from Models import models
from database.database import engine


app = FastAPI(
    title="PixiePlace"
)

models.Base.metadata.create_all(bind=engine)
app.include_router(auth_router)
app.include_router(root_router)


