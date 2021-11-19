#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: __init__.py.py
@time: 2021/11/19 10:53 上午
"""


class PostParamsError(Exception):
    def __init__(self, err_desc: str = "POST请求参数错误"):
        self.err_desc = err_desc


class TokenAuthError(Exception):
    def __init__(self, err_desc: str = "token认证失败"):
        self.err_desc = err_desc
