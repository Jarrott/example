# -*- encoding:utf-8 -*-
"""
@ Created by Seven on  2019/01/16 <https://www.soo9s.com>
"""
from app import create_app
from app.api.seven.models import db, User

"""创建超级管理员
"""

app = create_app()
with app.app_context():
    with db.auto_commit():
        user = User()
        user.nickname = "Admin"
        user.username = "jiandan"
        user.password = "jiandan"
        user.auth = 777
        db.session.add(user)

"""
主要是离线脚本
可以创建一些假的数据
"""