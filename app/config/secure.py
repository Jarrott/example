# -*- encoding:utf-8 -*-
"""
@ Created by Seven on  2019/01/21 <https://www.soo9s.com>
"""
SECRET_KEY = '7d58afd5-5fdb-48b0-9c99-3466c2838745'

# mysql 配置

SQLALCHEMY_TRACK_MODIFICATIONS = False  # 如果不设置会一直有个提示,源代码中是 None

# cymysql 驱动不要忘记装,不然不会报错.也不会成功创建表单的
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://{name}:{password}@sh-cdb-4r50kts5.sql.tencentcdb.com:63198/{db}' \
    .format(
    name='root', password='jiandan123*#', db='example-simple')
