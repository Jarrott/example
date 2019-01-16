# -*- encoding:utf-8 -*-
"""
@ Created by Seven on  2019/01/16 <https://www.soo9s.com>
"""
from flask import Blueprint
from app.api.seven.v1 import ()


def create_blueprint():
    """
    版本号为v1
    将宏图注册到蓝图当中
    :return: 视图路由
    """
    bp_v1 = Blueprint('seven_v1', __name__)
    # home.api.register(bp_v1)
    return bp_v1
