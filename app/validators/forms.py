# -*- encoding:utf-8 -*-
"""
@ Created by Seven on  2019/01/16 <https://www.soo9s.com>
"""
from flask_wtf.file import FileAllowed
from wtforms import (Form, StringField,
                     PasswordField, IntegerField,
                     FileField, SelectField)
from wtforms.validators import (DataRequired, Length, regexp, ValidationError)
from app.libs.auto_pro import get_data_cache
from app.libs.error_code import NotFound, ClientTypeError
from app import files
from app.api.seven.models import User, Role
from app.libs.enums import ClientTypeEnum
from app.libs.form_base import BaseForm


class ClientForm(BaseForm):
    """
    验证用户的登录信息
    """
    username = StringField(validators=[
        DataRequired(message="用户名不能为空"),
        Length(6, 32, message="用户名必须在6~32位之间")
    ])

    password = PasswordField(validators=[
        DataRequired(message="密码不能为空"),
        regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$', message='用户密码必须在6~22位之间')
    ])
    type = IntegerField(validators=[DataRequired(message="类型不能为空!")], default=100)
    code = StringField(validators=[DataRequired(message="请重新输入验证码!"), Length(4, 4)])

    def validate_type(self, value):
        try:
            client = ClientTypeEnm(value.data)
        except ValueError as e:
            raise e
        self.type.data = client

    def validate_code(self, value):
        uid = User.query.filter_by(username=self.username.data).first()
        s_code = value.data.lower()
        b_data = value.data.upper()
        if s_code is not b_data:
            code = get_data_cache(s_code)
            if code is None:
                raise ClientTypeError({"message": ["请重新输入验证码！"]})
            elif uid is None:
                raise NotFound(message={'message': ["用户不存在！"]})
            self.code.data = code


class UserForm(BaseForm):
    """
    验证注册
    """
    username = StringField(validators=[
        DataRequired(message="用户名不能为空"),
        Length(6, 32, message="用户名必须在6~32位之间")
    ])

    password = PasswordField(validators=[
        DataRequired(message="密码不能为空"),
        regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$', message='用户密码必须在6~22位之间')
    ])

    nickname = StringField(
        validators=[
            DataRequired(message="用户昵称不能为空"),
            Length(6, 32, message="用户昵称必须在6~32位之间")
        ])

    type = IntegerField(validators=[DataRequired(message="类型不能为空!")], default=100)

    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client

    def validate_username(self, value):
        """
        查询用户是否已经存在
        :param value:
        :return:
        """
        if User.query.filter_by(username=value.data).first():
            raise ValidationError('该用户已注册')

    def validate_nickname(self, value):
        """
        查询用户昵称是否已经存在
        :param value:
        :return:
        """
        if User.query.filter_by(nickname=value.data).first():
            raise ValidationError('该昵称已被占用')


class ChangePasswordForm(BaseForm):
    old_password = PasswordField('原密码', validators=[DataRequired(message="不能为空！")])
    new_password = PasswordField('新密码',
                                 validators=[DataRequired(message="不能为空！"), Length(6, 32, message="密码必须在6~32位之间")])


class ChangeMyself(BaseForm):
    image = StringField(validators=[DataRequired(message="图片不能为空！")])
    nickname = StringField(validators=[DataRequired(message="昵称不能为空！"), Length(6, 32, message="昵称必须在6~32位之间")])

    def validate_nickname(self, value):
        """
        查询用户昵称是否已经存在
        :param value:
        :return:
        """
        if User.query.filter_by(nickname=value.data).first():
            raise ValidationError('该昵称已被占用')

    def validate_for_edit(self, value, data):
        nickname_count = User.query.filter_by(nickname=value).count()
        if nickname_count == 1 and data.nickname != value:
            ''' != value["company"] 代表是修改了，并且和数据库有重复 '''
            raise ValidationError("昵称已存在！")


class SearchDataQForm(BaseForm):
    """搜索用到的关键字和时间"""
    start_time = StringField()
    end_time = StringField()
    q = StringField()
    sort = StringField()
    operator = StringField()
    type = StringField()
    page_num = IntegerField(default=1)
    page_size = IntegerField()
    state = StringField()


class UploadForm(BaseForm):
    """上传文件"""
    files = FileField(validators=[FileAllowed(files, message="文件格式不正确！"), DataRequired(message="文件不能为空！")])
