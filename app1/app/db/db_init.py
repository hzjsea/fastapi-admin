#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: db_init.py
@time: 2021/11/19 2:19 下午
@description:

网上很多对sqlalchemy的封装是采用上下文管理器来管理连接池的，比如像这样封装你一个上下文管理器

session_factory = sessionmaker(bind=ENGINE,autocommit=False,autoflush=False)

@contextmanager
def session_maker():
    session = session_factory()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        logger.error(f"[DATABASE ERROR] {e}")
    finally:
        session.close()

with session_maker() as session:
        result = session.query(MinerTable).all()
        for item in result:
            data.append(item.asdict())

每次调用的时候都会生成一份session， 在离开上下文管理后， 会自动关闭session, 因此在整个项目代码中，都会有一份
session在被不断地调用， 但这仅仅只支持同步的代码，如果一个接口中有多个逻辑，多次调用with后，会出现阻塞的问题，也就是
前一份内容的session还没被关闭，后面上下文又再次来调用，一旦时间长了，或者高频率调用接口， 累计的session数量过多，就会让程序挂掉


fastapi中的接口都支持异步调用，同时接口也支持依赖注入，在一份接口中只需要使用一份session的连接，接口调用结束之后，会自动丢弃这一份session
本项目模板主要使用这种方式


"""
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from ..settings import config2
import redis

engine = create_engine(config2.SQLALCHEMY_DATABASE_URI)

LocalSession = sessionmaker(
    bind=engine,
    autocommit=False,  # 关闭自动提交
    autoflush=False,  # 关闭自动刷新
)


# Base = declarative_base()

# def get_db() -> Generator:
#     """
#     返回一个生成器
#     该方法提供给依赖注入使用
#     :return:
#     """
#     try:
#         db = session()
#         yield db
#     finally:
#         db.close()


# redis init
pool = redis.ConnectionPool(
    host=config2.REDIS_HOST,
    port=6379,
    db=0,
    password=123456,
    decode_responses=True
)

r = redis.Redis(connection_pool=pool)
