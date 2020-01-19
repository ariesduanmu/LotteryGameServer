# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2019-12-12 18:53:56
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-01-19 13:26:05
from . import app

from numpy.random import choice

from bottle import response
from bottle import request

from sql.user import User
from sql.gamerule import GameRule
from sql.lottery import Lottery

from .utils import data_2_json
from .utils import parse_qsl
from .utils import touni


@app.post('/lottery')
def lottery(db):
    '''
    Args:
        username
    Return:
        image: base后的图片数据
        name: 名字
        candidate_id
        candidate_prize
        prize
            id
            name
            image_name
        lottery_time
        failed_lottery: 抽奖失败的次数
        did_win: 1、之前已中奖; 0、之前未中奖

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

    if not user:
        return data_2_json(1003, errmsg="user not exist")

    if not game_rule:
        return data_2_json(1002, errmsg="fail to lottery")

    lottery_time = game_rule.max_lottery - user.did_lottery

    if lottery_time <= 0:
        return data_2_json(1004, errmsg="no lottery time available")

    user.lotter()
    user.recent_login()

    lottery_info = db.query(Lottery).filter_by(user_id=user.id).first()

    data = {}
    data['win'] = 0

    if not lottery_info:

        win_probability = game_rule.win_probability / 100
        casino = choice([0,1], 1, p=[1-win_probability, win_probability])[0]

        # 中奖概率为0
        if casino == 1:
            lottery_info = Lottery(user.id)
            db.add(lottery_info)
            data['win'] = 1
    
    return data_2_json(1000, content=data)



        
