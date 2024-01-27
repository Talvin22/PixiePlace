from fastapi import APIRouter
from sqlalchemy import select, insert
from starlette import status

from Auth.auth import auth_router, db_dependency
from Models import models
from database.database import engine
from Root.schemas import Suppliers

root_router = APIRouter(
    prefix="/main",
    tags=["Main"]
)
models.Base.metadata.create_all(bind=engine)

@root_router.get("/", status_code=status.HTTP_200_OK)
def main(db: db_dependency):
    query = db.query(models.Products).all()
    return query

@root_router.post("/", status_code=status.HTTP_200_OK)
def test_add_supplier(new_sup: Suppliers, db: db_dependency):
    stmt = insert(models.Suppliers).values(**new_sup.model_dump())
    db.execute(stmt)
    db.commit()
    return {"status":"200"}