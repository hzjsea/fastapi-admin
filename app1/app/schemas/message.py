#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: message.py
@time: 2021/12/1 5:20 下午
"""

from pydantic import BaseModel

class Msg(BaseModel):
    msg: str