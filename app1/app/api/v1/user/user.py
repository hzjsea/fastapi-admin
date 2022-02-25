#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: user.py
@time: 2021/11/19 10:45 上午
"""

from fastapi import APIRouter, Body, Depends, HTTPException
from app1.app.utils.responses import response_code as c
from typing import List
from app1.app import schemas
# from

router = APIRouter()

# @router.get("/", response_model=List[schemas.User])
# def get_users(
#     db: Session = Depends()
# )