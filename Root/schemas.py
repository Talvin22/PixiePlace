from pydantic import BaseModel

class Suppliers(BaseModel):

    id : int
    company_name : str
    email : str
    phone_number : str
    address : str


class Categories(BaseModel):

    id : int
    name :str


class Subcategories(BaseModel):

    id :int
    name : str
    category_id : int


class Products(BaseModel):
    id: int
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
