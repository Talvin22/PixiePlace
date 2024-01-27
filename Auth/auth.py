from datetime import timedelta, datetime
from typing import Annotated, Optional

from fastapi import APIRouter, Depends, HTTPException
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from Auth.schemas import CreateUserRequest, Token
from Models import models

from Models.models import Users
from database.database import SessionLocal, engine
from jose import jwt, JWTError
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("ALGORITHM")
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={401: {"user": "Not authorised"}}
)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
models.Base.metadata.create_all(bind=engine)


def get_password_hash(password):
    return bcrypt_context.hash(password)


def verify_password(plain_password, hashed_password):
    return bcrypt_context.verify(plain_password, hashed_password)


def authenticate_user(username: str, password: str, db):
    user = db.query(models.Users) \
        .filter(models.Users.username == username) \
        .first()

    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(username: str, user_id: int,
                        expires_delta: Optional[timedelta] = None):
    encode = {"sub": username, "id": user_id}
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    encode.update({"exp": expire})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


async def det_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        if user_id is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Could not validate user.")
        return {"username": username, "id": user_id}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Could not validate user.")


@auth_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: CreateUserRequest):
    try:
        # user_model = db.query(Users).filter(Users.id == create_user_req.id).first()
        create_user_model = Users(
            username=create_user_request.username,
            email=create_user_request.email,
            phone_number=create_user_request.phone_number,
            first_name=create_user_request.first_name,
            last_name=create_user_request.last_name,
            hashed_password=bcrypt_context.hash(create_user_request.password),
            is_admin=False

        )
        db.add(create_user_model)
        db.commit()
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="User already exists")


@auth_router.post("/login", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Could not validate user.")
    token = create_access_token(user.username, user.id, timedelta(minutes=20))
    return {"access_token": token,
            "token_type": "bearer"}
