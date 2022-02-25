#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: user.py.py
@time: 2021/11/19 1:53 下午
"""

from typing import TYPE_CHECKING
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app1.app.db import Base

# 跳过类型检查， 解决循环导入的问题
if TYPE_CHECKING:
    from .item import ItemModel


class UserModel(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(64), index=True)
    description = Column(String(64), index=True)
