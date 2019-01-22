# -*- encoding:utf-8 -*-
"""
@ Created by Seven on  2019/01/21 <https://www.soo9s.com>
"""
from flask import jsonify
from jian.redprint import Redprint
from jian.interface import UserInterface

api = Redprint('user')


@api.route('', methods=['GET'])
def index():
    user = UserInterface()
    user.get()
    return jsonify({
        "success": 200
    })
