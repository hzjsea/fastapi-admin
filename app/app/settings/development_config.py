#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: development_config.py.py
@time: 2021/11/19 10:04 上午
"""

"""

开发环境配置

"""
import secrets
from typing import Any, Dict, Optional, Union
from pydantic import AnyHttpUrl, BaseSettings, EmailStr, validator, IPvAnyAddress


class Config(BaseSettings):
    # 文档地址
    DOCS_URL: str = "/api/v1/docs"
    # # 文档关联请求数据接口
    OPENAPI_URL: str = "/api/v1/openapi.json"
    # 禁用 redoc 文档
    REDOC_URL: Optional[str] = None

    SERVER_NAME: str = 'test'
    SERVER_HOST: AnyHttpUrl = 'http://127.0.0.1'
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    # SECRET_KEY: str = 'aeq)s(*&dWEQasd8**&^9asda_asdasd*&*&^+_sda'

    # 配置Mysql
    MYSQL_USERNAME: str = 'root'
    MYSQL_PASSWORD: str = ""
    MYSQL_HOST: Union[AnyHttpUrl, IPvAnyAddress] = "127.0.0.1"
    MYSQL_DATABASE: str = 'fast'

    # Mysql地址
    SQLALCHEMY_DATABASE_URI = f"mysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@" \
                              f"{MYSQL_HOST}/{MYSQL_DATABASE}?charset=utf8"

    PROJECT_NAME: str = 'fast_api'

    SMTP_TLS: bool = True
    SMTP_PORT: Optional[int] = None
    SMTP_HOST: Optional[str] = None
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAILS_FROM_EMAIL: Optional[EmailStr] = None
    EMAILS_FROM_NAME: Optional[str] = None

    @validator("EMAILS_FROM_NAME")
    def get_project_name(cls, v: Optional[str], values: Dict[str, Any]) -> str:
        if not v:
            return values["PROJECT_NAME"]
        return v

    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48
    EMAIL_TEMPLATES_DIR: str = "/app/email-templates/build"
    EMAILS_ENABLED: bool = False

    @validator("EMAILS_ENABLED", pre=True)
    def get_emails_enabled(cls, v: bool, values: Dict[str, Any]) -> bool:
        return bool(
            values.get("SMTP_HOST")
            and values.get("SMTP_PORT")
            and values.get("EMAILS_FROM_EMAIL")
        )

    EMAIL_TEST_USER: EmailStr = "test@example.com"  # type: ignore
    FIRST_SUPERUSER: EmailStr = 'test@example.com'
    FIRST_SUPERUSER_PASSWORD: str = '123456'
    USERS_OPEN_REGISTRATION: bool = True


config2 = Config()
