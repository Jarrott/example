# -*- encoding:utf-8 -*-
"""
@ Created by Seven on  2019/01/22 <https://www.soo9s.com>
"""
from app.app import create_app
from jian.db import db
from jian.core import User

app = create_app()
with app.app_context():
    with db.auto_commit():
        # 创建一个超级管理员
        user = User()
        user.nickname = 'super'
        user.password = 'simple'
        user.email = '1234995678@qq.com'
        # super为 2 的时候为超级管理员，普通用户为 1
        user.super = 2
        db.session.add(user)
