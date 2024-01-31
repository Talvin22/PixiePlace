from fastapi import APIRouter, Query, Depends
from starlette import status

from typing import Annotated
from Auth.schemas import User

from Auth.auth import router, db_dependency, get_current_user, login_for_access_token
from Models import models
from database.database import engine

import re

root_router = APIRouter(
    prefix="/main",
    tags=["Main"]
)
models.Base.metadata.create_all(bind=engine)


@root_router.get("/", status_code=status.HTTP_200_OK)
def main(db: db_dependency):
    prod = db.query(models.Products).all()  # [:2]
    cat = db.query(models.Categories).all()
    # token = login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency)[0]
    # user = det_current_user(token)
    return {"products": prod, "categories": cat}  # ,"curent user":user}


@root_router.get("/{category_name}", status_code=status.HTTP_200_OK)
def category(db: db_dependency, category_name: str):
    cat = db.query(models.Categories).where(models.Categories.name == category_name).first()

    prod = db.query(models.Products).where(models.Products.category_id == cat.id).all()
    return {"products": prod, "categories": cat}


@root_router.get("/users/me/", response_model=User)
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user


@root_router.get("/q/{query}", status_code=status.HTTP_200_OK)
def search(db: db_dependency, q: str = Query(..., min_length=3, title="Search Query")):
    results = []
    pattern = re.compile(fr'\b{re.escape(q)}\b', re.IGNORECASE)
    prod = list(db.query(models.Products).all())
    # # prod2 = db.execute(**db.query(models.Products).where((models.Products.title.ilike(f"%{q}%")) | (models.Products.description.ilike(f"%{q}%")))).fetchall()
    print(prod[0], type(prod))
    for product in prod:
        if pattern.search(product.title) or pattern.search(product.description):
            results.append(product)
    # prod = db.query(models.Products).where(models.Products.title==q).all()
    return {"result": results}
