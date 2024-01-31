from datetime import datetime
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, BLOB, Float, TIMESTAMP, JSON, LargeBinary, \
    MetaData, Table
from sqlalchemy.orm import mapped_column

metadata = MetaData()

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, unique=True),
    Column("phone_number", String, unique=True),
    Column("username", String, unique=True),
    Column("first_name", String),
    Column("last_name", String),
    Column("hashed_password", String),
    Column("role", String),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False)

)

supplier = Table(
    "supplier",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("company_name", String, unique=True, nullable=False),
    Column("email", String, unique=True, nullable=False),
    Column("phone_number", String, unique=True, nullable=False),
    Column("address", String, nullable=False)

)

category = Table(
    "category",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False)
)

subcategory = Table(
    "subcategory",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, unique=True, nullable=False),
    Column("category_id", Integer, ForeignKey(category.c.id))
)

product = Table(
    "product",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, unique=True, nullable=False),
    Column("description", String, nullable=False),
    Column("photo", LargeBinary, nullable=False),
    Column("on_sale", Boolean, default=False),
    Column("price", Integer, nullable=False),
    Column("characteristic", String, nullable=False),
    Column("mark", Float, nullable=True),
    Column("in_stock", Boolean, default=True),
    Column("size", String, nullable=False),
    Column("supplier_id", Integer, ForeignKey(supplier.c.id)),
    Column("category_id", Integer, ForeignKey(category.c.id))
)

comment = Table(
    "comment",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("text", String, nullable=False),
    Column("photo", LargeBinary, nullable=True),
    Column("date", TIMESTAMP, default=datetime.utcnow()),
    Column("mark", Float, nullable=True),
    Column("product_id", Integer, ForeignKey(product.c.id)),
    Column("user_id", Integer, ForeignKey(user.c.id))
)

cart = Table(
    "cart",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("product_id", Integer, ForeignKey(product.c.id)),
    Column("user_id", Integer, ForeignKey(user.c.id))
)

message = Table(
    "message",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("data", JSON, nullable=False),
    Column("user_id", Integer, ForeignKey(user.c.id))
)

answer = Table(
    "answer",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("data", JSON, nullable=False),
    Column("user_id", Integer, ForeignKey(user.c.id))
)

product_photo = Table(
    "product_photo",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("photo", LargeBinary, nullable=True),
    Column("product_id", Integer, ForeignKey(product.c.id)),
)

# class Users(Base):
#     __tablename__ = "users"
#
#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True)
#     phone_number = Column(String, unique=True, index=True)
#     username = Column(String, unique=True, index=True)
#     first_name = Column(String)
#     last_name = Column(String)
#     hashed_password = Column(String)
#     role = Column(String, default=False)
#
#
# class Suppliers(Base):
#     __tablename__ = "suppliers"
#
#     id = Column(Integer, primary_key=True, index=True)
#     company_name = Column(String, unique=True)
#     email = Column(String, unique=True, index=True)
#     phone_number = Column(String, unique=True, index=True)
#     address = Column(String, nullable=False)
#
#
# class Categories(Base):
#     __tablename__ = "categories"
#
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False)
#
#
# class Subcategories(Base):
#     __tablename__ = "subcategories"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False)
#     category_id = Column(Integer, ForeignKey("categories.id"))
#
#
# class Products(Base):
#     __tablename__ = "products"
#
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, nullable=False)
#     description = Column(String, nullable=False)
#     photo = Column(LargeBinary, nullable=True)
#     on_sale = Column(Boolean, default=False)
#     price = Column(Integer, nullable=False)
#     characteristic = Column(String, nullable=False)
#     mark = Column(Float, nullable=True)
#     in_stock = Column(Boolean, default=True)
#     size = Column(String, nullable=False)
#     supplier_id = Column(Integer, ForeignKey("suppliers.id"))
#     category_id = Column(Integer, ForeignKey("categories.id"))
#
#
# class Comments(Base):
#     __tablename__ = "comments"
#
#     id = Column(Integer, primary_key=True, index=True)
#     text = Column(String, nullable=False)
#     photo = Column(LargeBinary, nullable=True)
#     date = Column(TIMESTAMP, default=datetime.utcnow())
#     mark = Column(Float, nullable=True)
#     product_id = Column(Integer, ForeignKey("products.id"))
#     user_id = Column(Integer, ForeignKey("users.id"))
#
#
# class Cart(Base):
#     __tablename__ = "cart"
#
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     product_id = Column(Integer, ForeignKey("products.id"))
#
#
# class Messages(Base):
#     __tablename__ = "messages"
#
#     id = Column(Integer, primary_key=True, index=True)
#     data = Column(JSON, nullable=False)
#     user_id = Column(Integer, ForeignKey("users.id"))
#
#
# class Answers(Base):
#     __tablename__ = "answers"
#
#     id = Column(Integer, primary_key=True, index=True)
#     data = Column(JSON, nullable=False)
#     user_id = Column(Integer, ForeignKey("users.id"))
#
#
# class ProductPhotos(Base):
#     __tablename__ = 'product_photos'
#
#     id = Column(Integer, primary_key=True, index=True)
#     photo = Column(LargeBinary, nullable=False)
#     product_id = Column(Integer, ForeignKey("products.id"))
