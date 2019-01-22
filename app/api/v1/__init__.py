# -*- encoding:utf-8 -*-
"""
@ Created by Seven on  2019/01/21 <https://www.soo9s.com>
"""
from flask import Blueprint
from app.api.v1 import user


def create_v1():
    bp_v1 = Blueprint('v1', __name__)
    user.api.register(bp_v1)
    return bp_v1
