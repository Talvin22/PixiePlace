from fastapi import APIRouter
from sqlalchemy import insert
from starlette import status

from Admin.schemas import Suppliers, Categories, Subcategories, Products
from Auth.auth import db_dependency
from Models import models
from database.database import engine

admin_router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)
models.Base.metadata.create_all(bind=engine)

@admin_router.post("/add_sup", status_code=status.HTTP_201_CREATED)
def test_add_supplier(new_sup: Suppliers, db: db_dependency):
    stmt = insert(models.Suppliers).values(**new_sup.model_dump())
    db.execute(stmt)
    db.commit()


@admin_router.post("/add_cat", status_code=status.HTTP_201_CREATED)
def test_add_cat(new_cat: Categories, db: db_dependency):
    stmt = insert(models.Categories).values(**new_cat.model_dump())
    db.execute(stmt)
    db.commit()


@admin_router.post("/add_sub", status_code=status.HTTP_201_CREATED)
def test_add_sub(new_cat: Subcategories, db: db_dependency):
    stmt = insert(models.Subcategories).values(**new_cat.model_dump())
    db.execute(stmt)
    db.commit()


@admin_router.post("/add_prod", status_code=status.HTTP_201_CREATED)
def test_add_prod(new_prod: Products, db: db_dependency):
    stmt = insert(models.Products).values(**new_prod.model_dump())
    db.execute(stmt)
    db.commit()
