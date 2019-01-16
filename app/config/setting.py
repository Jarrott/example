# -*- encoding:utf-8 -*-
"""
@ Created by Seven on  2019/01/16 <https://www.soo9s.com>
"""

# 基本配置
import os

DEBUG = True
JSON_AS_ASCII = False
# Swagger 配置+跨域请求

SWAGGER = {
    "swagger_version": "2.0",
    "title": "大数据平台项目",
    "specs": [
        {
            "version": "0.5",
            "title": "主页API接口列表",
            "description": 'This is the version 0.5 of Big-data API',
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
        }
    ],
}
DOCUMENTS = tuple(
    'jpg jpe jpeg png gif svg bmp doc docx xls xlsx'.split())  # 允许上传的文件类型

PER_PAGE = 10

# Token 过期时间
JWT_TOKEN_EXPIRES = 1 * 24 * 3600
