from datetime import datetime
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, BLOB, Float, TIMESTAMP, JSON
from sqlalchemy.orm import relationship
from database.database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_admin = Column(Boolean, default=False)


class Suppliers(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, unique=True)
    email = Column(String, unique=True, index=True)
    hone_number = Column(String, unique=True, index=True)
    address = Column(String, nullable=False)


class Categories(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)


class Subcategories(Base):
    __tablename__ = "subcategories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"))


class Comments(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    photo = Column(BLOB, nullable=True)
    date = Column(TIMESTAMP, default=datetime.utcnow())
    mark = Column(Float, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))


class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    photo = Column(BLOB, nullable=True)
    on_sale = Column(Boolean, default=False)
    price = Column(Integer, nullable=False)
    characteristic = Column(String, nullable=False)
    mark = Column(Float, nullable=True)
    in_stock = Column(Boolean, default=True)
    size = Column(String, nullable=False)
    comment_id = Column(String, ForeignKey("comments.id"))
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))


class Cart(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))


class Messages(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(JSON, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))


class Answers(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(JSON, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))


class ProductPhotos(Base):
    __tablename__ = 'product_photos'

    id = Column(Integer, primary_key=True, index=True)
    photo = Column(BLOB, nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"))

