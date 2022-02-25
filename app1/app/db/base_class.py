#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: base_class.py
@time: 2021/11/19 2:05 下午
"""
from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import Column, TIMESTAMP, DateTime, func, String


@as_declarative()
class Base:
    """
    Model 类初始类
    """
    id: Any
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    # 所有的类都会有这两个字段
    white = Column(String, nullable=False, default="")
    create_time = Column(DateTime, nullable=False, server_default=func.now())
    update_time = Column(TIMESTAMP, nullable=False)
