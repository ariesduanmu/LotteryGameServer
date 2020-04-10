# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2019-12-12 18:53:56
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-10 12:39:06
from . import app

from numpy.random import choice

from bottle import response
from bottle import request

from sql.gamerule import GameRule


from .utils import data_2_json
from .utils import parse_qsl
from .utils import touni


@app.post('/lottery')
def lottery(db):
    '''
    Args:
    
    ::parameter username:: your name
    ::parameter type:: str
    
    Return:

    ::parameter username:: your name
    ::parameter type:: str

    ::parameter win:: 1 for win, 0 for lost
    ::parameter type:: int

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

    game_rule = db.query(GameRule).first()


    if not game_rule:
        game_rule = GameRule(50)
        db.add(game_rule)
        db.commit()
        db.flush()
        

    data = {}
    data['username'] = username

    win_probability = game_rule.win_probability / 100
    is_win = choice([0,1], 1, p=[1-win_probability, win_probability])[0]
    data['win'] = str(is_win)

    return data_2_json(1000, content=data)



        
