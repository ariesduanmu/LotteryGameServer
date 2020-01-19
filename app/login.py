# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2019-12-12 18:53:24
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-01-19 13:26:33
from . import app

from sql.user import User
from sql.gamerule import GameRule
from sql.lottery import Lottery

from bottle import request
from bottle import response

from .utils import data_2_json
from .utils import parse_qsl
from .utils import touni

@app.post('/login')
def login(db):
    '''User login
    Args:
        username: if username not exist, regist
    Return:
        lottery_time: lottery times left
        did_win: did user win in lottery
    '''
    response.content_type = 'application/json'

    if request.content_type == 'application/json':
        parameter_dic = request.json
    else:
        # parameter_dic = request.POST
        
        # parse in utf8
        parameter_dic = {}

        body = touni(request.body.read(102400), 'utf8')
        for key, value in parse_qsl(body):
            parameter_dic[key] = value

    username = parameter_dic.get('username')

    if not username:
        return data_2_json(1001, errmsg="need username") 

    user = db.query(User).filter_by(username=username).first()
    game_rule = db.query(GameRule).first()

    # can not continue without game rule
    if not game_rule:
        return data_2_json(1002, errmsg="fail to login") 

    did_win = 0
    lottery_time = game_rule.max_lottery

    if user:
        lottery_time = max(0, game_rule.max_lottery - user.did_lottery)
        user.recent_login()
        
        lottery_info = db.query(Lottery).filter_by(user_id=user.id).all()
        if lottery_info:
            did_win = 1

    else:
        user = User(username)
        db.add(user) 

    data = {
                'lottery_time':lottery_time, 
                'did_win':did_win
            }

    return data_2_json(1000, content=data)