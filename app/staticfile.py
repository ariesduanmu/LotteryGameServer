# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-01-07 11:47:40
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-01-19 13:22:45
from bottle import static_file
from config.utils import IMAGE_PATH
from . import app

@app.get('/images/<dirname>/<filename>')
def server_static(dirname, filename):
    return static_file(filename, root=f"{IMAGE_PATH}/{dirname}")