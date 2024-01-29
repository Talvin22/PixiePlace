from fastapi import APIRouter
from sqlalchemy import select, insert
from starlette import status

from Auth.auth import auth_router, db_dependency, det_current_user, login_for_access_token
from Models import models
from database.database import engine
from Single.schemas import *



single_router = APIRouter(
    prefix="/single",
    tags=["Single_product"]
)
models.Base.metadata.create_all(bind=engine)

@single_router.get("/{product_title}/{product_id}")
def single_product(product_title: str, product_id: int, db: db_dependency):
    prod = db.query(models.Products).where(models.Products.id == product_id).first()
    sim = db.query(models.Products).where(models.Categories.id==prod.category_id).all()[:5]
    cat = db.query(models.Categories).where(models.Categories.id == prod.category_id).all()
    com = db.query(models.Comments).where(models.Comments.product_id==product_id).all()
    supp = db.query(models.Suppliers).where(models.Suppliers.id==prod.supplier_id).all()
    pho = db.query(models.ProductPhotos).where(models.ProductPhotos.product_id==product_id).all()
    return {"product":prod,"similar products":sim,"category":cat,"commentaries":com,"suppliers":supp,"photos":pho}

@single_router.post("/add_com", status_code=status.HTTP_201_CREATED)
def test_add_comments(new_com: Comments, db: db_dependency):
    stmt = insert(models.Comments).values(**new_com.model_dump())
    db.execute(stmt)
    db.commit()
