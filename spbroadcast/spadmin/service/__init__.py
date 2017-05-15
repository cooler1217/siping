#!/usr/bin/env python2.7
# coding=utf-8
"""
Created on 2014-12-9

@author: cooler
"""

from flask import Flask
from admin import admin

DEFAULT_APP_NAME = 'BEEHOO'

DEFAULT_MODULES = (
    (admin, '/admin'),
)


def create_app():
    """ 创建、初始化app """
    app = Flask(DEFAULT_APP_NAME)
    # 使用flask中的Blueprint设置站点模块
    setting_modules(app, DEFAULT_MODULES)
    return app


def setting_modules(app, modules):
    """ 注册Blueprint模块 """
    for module, url_prefix in modules:
        # 通过register_blueprint注册
        app.register_blueprint(module, url_prefix=url_prefix)
