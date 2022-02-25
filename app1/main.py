#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: main.py
@time: 2021/11/19 10:06 上午
"""

from app.api import create_app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app='main:app', host="127.0.0.1", port=8010, reload=True, debug=True, workers=2, timeout_keep_alive=3)
