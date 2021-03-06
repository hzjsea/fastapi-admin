#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: hello.py
@time: 2021/11/19 10:34 上午
"""

from fastapi import APIRouter
from app1.utils.responses.xhr import response_ok, response_error

router = APIRouter()


@router.get("/hello", summary="hello get请求格式")
async def hello():
    data = {
        "hahaha": "hello word!"
    }

    return response_ok(data)


@router.post("/hello", summary="hello post请求格式")
async def hello():
    data = "hello word!"
    return response_ok(data)


@router.put("/hello", summary="hello put请求格式")
async def hello():
    data = "hello word!"
    return response_ok(data)


@router.delete("/hello", summary="hello delete请求格式")
async def hello():
    data = "hello word!"
    return response_ok(data)