#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: __init__.py.py
@time: 2021/11/19 10:09 上午
"""
import traceback

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exception_handlers import request_validation_exception_handler
from fastapi.exceptions import RequestValidationError
# from app1.settings import setting  # 导入环境的方式1
from app1.app.settings import config2 # 导入环境的方式2
from app1.app.api.v1 import api, prefix
from app1.app.utils.custom_exc import PostParamsError
from app1.app.logsX import logger

tags_metadata = [
    {
        "name": "API",
        "description": "数据接口API"
    }
]


def create_app():
    app = FastAPI(
        title="项目名称",
        description="项目描述",
        version="项目版本",
        docs_url=config2.DOCS_URL, # 文档地址
        openapi_url=config2.OPENAPI_URL,
        redoc_url=config2.REDOC_URL,
        openapi_tags=tags_metadata

    )

    app.include_router(
        api,
        prefix=prefix
        # tags=["items"]
        # dependencies = [Depends(get_token_header)]
        # responses={404: {"description": "Not found"}},
    )

    register_exception(app)  # 注册捕获异常信息
    register_cors(app)  # 注册跨域请求

    return app


def register_exception(app: FastAPI):
    """
    全局异常捕获
    :param app:
    :return:
    """

    # 捕获自定义异常
    @app.exception_handler(PostParamsError)
    async def query_params_exception_handler(request: Request, exc: PostParamsError):
        """
        捕获 自定义抛出的异常
        :param request:
        :param exc:
        :return:
        """
        logger.error(f"参数查询异常\nURL:{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"code": 400, "data": {"tip": exc.err_desc}, "message": "fail"},
        )

    # @app.exception_handler(TokenAuthError)
    # async def token_exception_handler(request: Request, exc: TokenAuthError):
    #     logger.error(f"参数查询异常\nURL:{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")
    #     return JSONResponse(
    #         status_code=status.HTTP_400_BAD_REQUEST,
    #         content={"code": 400, "data": None, "message": exc.err_desc},
    #     )

    # 捕获参数 验证错误
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        """
        捕获请求参数 验证错误
        :param request:
        :param exc:
        :return:
        """
        # logger.error(f"参数错误\nURL:{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")
        # return JSONResponse(
        #     status_code=status.HTTP_400_BAD_REQUEST,
        #     content=jsonable_encoder({"code": 400, "data": {"tip": exc.errors()}, "body": exc.body, "message": "fail"}),
        # )
        data = {"tip": exc.errors()}
        # print(exc.errors())
        # return UJSONResponse(response_error(data=data, message="参数错误"))
        return await request_validation_exception_handler(request, exc)
        # return UJSONResponse()

    # 捕获全部异常
    @app.exception_handler(Exception)
    async def all_exception_handler(request: Request, exc: Exception):
        logger.error(f"全局异常\nURL:{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"code": 500, "data": {"tip": "服务器错误"}, "message": "fail"},
        )


def register_cors(app: FastAPI):
    """
    支持跨域

    貌似发现了一个bug
    https://github.com/tiangolo/fastapi/issues/133

    :param app:
    :return:
    """

    app.add_middleware(
        CORSMiddleware,
        # allow_origins=['http://localhost:8081'],  # 有效, 但是本地vue端口一直在变化, 接口给其他人用也不一定是这个端口
        # allow_origins=['*'],   # 无效 bug allow_origins=['http://localhost:8081']
        # allow_origin_regex='https?://.*',  # 改成用正则就行了
        allow_origin_regex='http?://.*',
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def register_middleware(app: FastAPI):
    """
    请求响应拦截 hook

    https://fastapi.tiangolo.com/tutorial/middleware/
    :param app:
    :return:
    """

    @app.middleware("http")
    async def logger_request(request: Request, call_next):
        # https://stackoverflow.com/questions/60098005/fastapi-starlette-get-client-real-ip
        logger.info(f"访问记录:{request.method} url:{request.url}\nheaders:{request.headers.get('user-agent')}"
                    f"\nIP:{request.client.host}")

        response = await call_next(request)

        return response
