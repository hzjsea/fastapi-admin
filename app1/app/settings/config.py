#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: config.py.py
@time: 2021/11/18 5:50 下午
"""
import os.path

import toml
from typing import Any
import json

"""
配置文件的读取方式

1. 这种方式是读取在项目的固定位置放置一个配置文件夹，这里采用的配置文件是toml格式
2. 然后项目采用单例模式读取 该文件夹下面的配置文件，读取后运行对应的环境
3. 这份文件如果有敏感信息，可以完全脱离项目放置，只需要修改路径即可


当然还有更简单暴力的写法，直接获取环境变量，运行对应的环境

import os

# 获取环境变量
env = os.getenv("ENV", "")
if env:
    # 如果有虚拟环境 则是 生产环境
    print("----------生产环境启动------------")
    from .production_config import config
else:
    # 没有则是开发环境
    print("----------开发环境启动------------")
    from .development_config import config

"""

#
# def setting_parse(path: str = None) -> Any:
#     if path is None:
#         raise RuntimeError("settings file is not exist")
#     data = toml.load(path)
#     environment = os.environ.get("ENVIRONMENT", None)
#     if environment is None:
#         raise RuntimeError("please set environment in system")
#
#     print(f"-----------{environment}环境启动-----------")
#     data = data[environment]
#
#     return data
#
#
# path = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + "/pyproject.toml"
# try:
#     setting = setting_parse(path)
# except Exception as e:
#     setting = ""


if __name__ == '__main__':
    """
    How To Use:
        1. 设置环境变量 export ENVIRONMENT="dev"
        2. 导入setting from settings import setting
        3. dict to json  setting_json = json.dumps(setting)
        4. dict to json format input   print(json.dumps(setting, indent=4, sort_keys=True))
    """
    path = os.path.dirname(os.path.dirname(os.getcwd())) + "/pyproject.toml"
    setting = setting_parse(path)
    print(json.dumps(setting, indent=4, sort_keys=True))
