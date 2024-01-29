from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    username: str
    email: str
    phone_number: str
    first_name: str
    last_name: str
    password: str
    is_admin: bool


class Token(BaseModel):
    access_token: str
    token_type: str

class User(BaseModel):

    email : str
    phone_number : str
    username : str
    first_name : str
    last_name : str
    hashed_password : str
    is_admin : bool