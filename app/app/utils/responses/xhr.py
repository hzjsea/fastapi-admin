#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: xhr.py.py
@time: 2021/11/19 10:38 上午
"""


from typing import Union
from .response_code import OK, ERROR, MESSAGES


def response_ok(data: Union[list, dict, str] = None, *, message: str = "ok") -> dict:
    return {
        'code': OK,
        'msg': message,
        'data': data,
    }


def response_error(data: Union[list, dict, str] = None, *, message: str = "", code: int = ERROR) -> dict:
    if not message:
        message = MESSAGES.get(code)
    return {
        'code': code,
        'msg': message,
        'data': data,
    }
