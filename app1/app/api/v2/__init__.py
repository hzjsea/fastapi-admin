#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: __init__.py.py
@time: 2021/11/19 10:09 上午
"""
from fastapi import APIRouter
from .hello import hello_router
from .user import login_router
from .user import user_router


prefix = "/api/v2"
api = APIRouter()

api.include_router(hello_router, tags=["test模块API"], prefix="/hello")
api.include_router(login_router, tags=["登陆模块API"], prefix="/login")
api.include_router(user_router, tags=["用户模块API"], prefix="/user")
