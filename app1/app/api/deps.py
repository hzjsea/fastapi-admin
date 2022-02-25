#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: deps.py
@time: 2021/12/3 11:43 上午
"""

"""
固定接口，无论版本如何变换这些接口都可以重复使用
因此可以归为一类被调用

比如这里的用户注册登录流程
"""

from app1.app.db.db_init import LocalSession
from fastapi import Depends
from typing import Generator, Union, Any
from app1.app import models, schemas
from fastapi.security import OAuth2PasswordBearer
from app1.app.settings import config2
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from passlib.context import CryptContext
from pydantic import  ValidationError

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# https://fastapi.tiangolo.com/zh/tutorial/security/simple-oauth2/
reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{config2.API_V1_STR}/login/access-token"
)

from jose import jwt


def get_db() -> Generator:
    global db
    try:
        db = LocalSession()
        yield db
    except:
        db.close()


def get_current_user(db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)) -> models.UserModel:
    try:
        payload = jwt.decode(
            token, config2.SECRET_KEY, algorithms=["H256"]
        )
        token_data = schemas.TokenPayload(**payload)
        print(token_data)
    except (jwt.JWTError,ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )

    logging.info("更新成功")


def create_access_token(
        subject: Union[str, Any], expires_delta: timedelta = None
) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=config2.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    encode_jwt = jwt.encode(to_encode, config2.SECRET_KEY, algorithm="H256")
    return encode_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


if __name__ == '__main__':
    get_current_user()