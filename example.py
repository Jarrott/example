# -*- encoding:utf-8 -*-
"""
@ Created by Seven on  2019/01/21 <https://www.soo9s.com>
"""
from app.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
