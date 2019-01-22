# -*- encoding:utf-8 -*-
"""
@ Created by Seven on  2019/01/21 <https://www.soo9s.com>
"""
from flask import Flask
from jian import Jian


def register_blueprints(app):
    """
    注册蓝图
    """
    from app.api.v1 import create_v1
    app.register_blueprint(create_v1(), url_prefix='/v1')


def register_cors(app):
    """
    解决跨域问题
    """
    from flask_cors import CORS
    CORS(app)


def register_swagger(app):
    """
    注册swagger
    : 看需求使用
    """
    from flasgger import Swagger
    Swagger(app)
    pass


def create_db(app):
    """
    创建表单
    """
    from jian import db
    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')
    register_blueprints(app)
    Jian(app)
    register_cors(app)
    register_swagger(app)
    create_db(app)
    return app
