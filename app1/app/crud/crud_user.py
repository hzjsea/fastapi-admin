#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: crud_user.py
@time: 2021/12/1 5:54 下午
"""
from app1.app.crud.base import CRUDBase
# from app1.app.schemas import UserUpdate, UserBase, UserCreate

from app1.app.schemas import UserBase, UserUpdate, UserCreate, User

class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    pass


if __name__ == '__main__':
    print(UserCreate)