#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: item.py.py
@time: 2021/11/19 1:52 下午
"""
from typing import TYPE_CHECKING
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from app1.app.db import Base

if TYPE_CHECKING:
    from .user import UserModel


class ItemModel(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(64), index=True)
    description = Column(String(64), index=True)
    # owner_id = Column(Integer, ForeignKey("user.id"))
