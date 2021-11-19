#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: __init__.py.py
@time: 2021/11/18 5:49 下午
"""

from .config import setting
import os

env = os.getenv("ENV", "")
if env:
    # 如果存在env关键词，则是生产环境
    print("----------生产环境启动----------")
    from .production_config import config2
else:
    # 如果没有env关键词，则是开发环境
    print("----------开发环境启动----------")
    from .development_config import config2
