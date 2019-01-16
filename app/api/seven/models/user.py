# -*- encoding:utf-8 -*-
"""
@ Created by Seven on  2019/01/16 <https://www.soo9s.com>
"""
from flask import g
from werkzeug.security import generate_password_hash, check_password_hash

from app.libs.error_code import NotFound, AuthFailed
from app.libs.model_base import (db, Base,
                                 MixinModelJSONSerializer)


class User(Base, MixinModelJSONSerializer):
    id = db.Column(db.Integer, primary_key=True, doc="用户自增ID")
    username = db.Column(db.String(24), unique=True, nullable=True, doc="用户名")
    nickname = db.Column(db.String(24), unique=True, nullable=False, doc="用户昵称")
    auth = db.Column(db.SmallInteger, default=100)
    _password = db.Column('password', db.String(100), nullable=True, doc="用户密码")
    _image = db.Column('image', db.String(50))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), doc="用户权限组")

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, filename):
        self._image = filename

    def _set_fields(self):
        """
        数据序列化要隐藏的字段
        """
        self._exclude = ['password']

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)

    @staticmethod
    def register_by_username(username, password, nickname):
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.username = username
            user.password = password
            db.session.add(user)

    @staticmethod
    def verify(username, password):
        """
        验证用户的作用域
        """
        user = User.query.filter_by(username=username).first()
        if not user:
            raise NotFound(message={'message': ["用户名或密码错误 ~"]})
        if not user.check_password(password):
            raise AuthFailed()
        scope = 'AdminScope' if user.auth == 777 else 'UserScope'
        return {'uid': user.id, 'scope': scope}

    @staticmethod
    def change_password(old_password, new_password):
        """
        修改密码
        """
        uid = g.user.uid
        with db.auto_commit():
            user = User.query.get(uid)
            if not user:
                return False
            if user.check_password(old_password):
                user.password = new_password
                return True
            return False


class AdminModularAuth(Base, MixinModelJSONSerializer):
    """模块权限"""
    id = db.Column(db.Integer, primary_key=True, doc="权限自增ID")
    modular_name = db.Column(db.String(100), doc="权限模块名称")
    parent_modular = db.Column(db.String(100), doc="二级权限模块名称")
    master_modular = db.Column(db.String(100), doc="一级权限模块名称")
    auth_name = db.relationship('AdminAuth', backref='admin_modular_auth')


class AdminAuth(Base, MixinModelJSONSerializer):
    """权限模快"""
    id = db.Column(db.Integer, primary_key=True, doc="权限自增ID")
    auth_name = db.Column(db.String(100), doc="权限名称")
    url = db.Column(db.String(200), doc="权限地址")
    module_id = db.Column(db.Integer, db.ForeignKey('admin_modular_auth.id'), doc="模块权限组")


class Role(Base, MixinModelJSONSerializer):
    """角色模块"""
    id = db.Column(db.Integer, primary_key=True, doc="自增ID")
    name = db.Column(db.String(100), unique=True, doc="角色名")
    auths = db.Column(db.String(255), doc="权限列表")
    role = db.relationship("User", backref='role')
