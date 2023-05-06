from passlib.context import CryptContext
from typing import Any
from services.user.user_schema import UserCreate
from models import User


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_user(db: Any, user_create: UserCreate):
    db_user = User(
        username=user_create.username,
        password=pwd_context.hash(user_create.password1),
        email=user_create.email,
    )
    db.add(db_user)
    db.commit()
