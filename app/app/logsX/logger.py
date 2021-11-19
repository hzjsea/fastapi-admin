#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: logger.py
@time: 2021/11/19 10:56 上午
"""

import os
import time
from loguru import logger

"""
日志文件配置

fastapi 做的建议将日志设置成为全局对象
https://github.com/tiangolo/fastapi/issues/81#issuecomment-473677039


"""

basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# 定位到log日志文件
log_path = os.path.join(basedir, 'logs')

if not os.path.exists(log_path):
    os.mkdir(log_path)

log_path_error = os.path.join(log_path, f'{time.strftime("%Y-%m-%d")}_error.log')

# 日志简单配置
logger.add(log_path_error, rotation="12:00", retention="5 days", enqueue=True)


__all__ = ["logger"]
