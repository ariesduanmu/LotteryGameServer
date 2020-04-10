# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2019-12-12 17:14:32
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-10 12:22:34
import bottle
from app import app

if __name__ == "__main__":
    port = 8000
    bottle.run(app, server='gunicorn', host='0.0.0.0', port=port)