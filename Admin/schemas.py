from pydantic import BaseModel


class Suppliers(BaseModel):
    company_name: str
    email: str
    phone_number: str
    address: str


class Categories(BaseModel):
    name: str


class Subcategories(BaseModel):
    name: str
    category_id: int


class Products(BaseModel):
    title: str
    description: str
    photo: bytes
    on_sale: bool
    price: int
    characteristic: str
    mark: float
    in_stock: bool
    size: str
    supplier_id: int
    category_id: int
