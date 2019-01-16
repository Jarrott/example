# -*- encoding:utf-8 -*-
"""
@ Created by Seven on  2019/01/16 <https://www.soo9s.com>
"""

# 重要的基本配置
SECRET_KEY = '7d58afd5-5fdb-48b0-9c99-3466c2838745'

SQLALCHEMY_TRACK_MODIFICATIONS = True

# mysql 配置

SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://{name}:{password}@sh-cdb-4r50kts5.sql.tencentcdb.com:63198/{db}' \
    .format(
    name='', password='', db='example')

# 阿里云邮件服务
EMAIL_USERNAME = 'jiandan@soo9s.com'
EMAIL_PASSWORD = 'JIANdan147'
EMAIL_HOST = 'smtpdm.aliyun.com'

# redis 配置
REDIS_HOST = 'redis-19966.c1.asia-northeast1-1.gce.cloud.redislabs.com'
REDIS_PORT = '19966'
REDIS_DB = '0'
REDIS_PASSWORD = 'redis'
