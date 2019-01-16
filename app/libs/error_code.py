# -*- encoding:utf-8 -*-
"""
@ Created by Seven on  2019/01/16 <https://www.soo9s.com>
"""
from .error import JsonTypeException


class Success(JsonTypeException):
    """
    操作成功
    """
    code = 201
    message = {'message': ['ok']}
    error_code = 0


class DeleteSuccess(JsonTypeException):
    """
    删除成功
    因为204是 not content
    所以稍微违背rest开发原则
    采用202
    """
    code = 202
    message = {'message': ['删除成功']}
    error_code = 1


class ClientTypeError(JsonTypeException):
    """
    用户注册相关异常
    """
    code = 400
    message = {'message': ['请求参数错误 ~ ！ ╮(╯▽╰)╭ ']}
    error_code = 10008


class ServerError(JsonTypeException):
    """
    服务器异常
    """
    code = 500
    message = {'message': ['服务器异常！']}
    error_code = 10001


class ParameterException(JsonTypeException):
    """
    全局异常
    """
    code = 400
    message = {'message': ['非法参数 ~ ！ ╮(╯▽╰)╭ ']}
    error_code = 10008


class NotFound(JsonTypeException):
    """
    404错误
    """
    code = 404
    message = {'message': ['找不到当前资源 ~ ']}
    error_code = 10013


class AuthFailed(JsonTypeException):
    """
    授权失败
    """
    code = 401
    message = {'message': ['用户名或密码错误 ~']}
    error_code = 10005


class Forbidden(JsonTypeException):
    """
    无权限操作
    """
    code = 403
    message = {'message': ['您没有访问此功能的权限 ~']}
    error_code = 10005


class Failed(JsonTypeException):
    code = 404
    msg = {'message': ['失败的动作 ~']}
    error_code = 100012


class ImagesError(JsonTypeException):
    code = 400
    message = {'message': ['图片上传失败']}
    error_code = 20001
