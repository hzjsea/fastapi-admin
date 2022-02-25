#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: user.py
@time: 2021/12/1 5:21 下午
"""

from pydantic import BaseModel, EmailStr
from typing import Optional
from devtools import debug

"""
Business Logic Model
"""


class UserBase(BaseModel):
    # email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    name: Optional[str] = None


class UserCreate(UserBase):
    # email: EmailStr
    password: str

    class Config:
        error_msg_templates = {
            'value_error.email': 'email格式错误'
        }


class UserUpdate(UserBase):
    password: Optional[str] = None


"""
DATABASE MODEL
"""


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class User(UserInDBBase):
    pass


if __name__ == '__main__':
    debug(UserInDBBase)
