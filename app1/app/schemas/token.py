#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: token.py
@time: 2021/12/1 5:21 下午
"""

from typing import Optional
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    sub: Optional[int] = None
