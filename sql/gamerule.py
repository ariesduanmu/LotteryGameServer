# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2019-12-25 10:34:21
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-10 12:34:04
from sql import Base

from sqlalchemy import Column
from sqlalchemy import Integer


class GameRule(Base):
    __tablename__ = 'game_rule'
    id = Column(Integer, primary_key=True, autoincrement=True)
    win_probability = Column(Integer, default=20, comment='获奖的概率')

    def __init__(self, win_probability):
        self.win_probability = win_probability

    def __repr__(self):
        return f"<GameRule(win_probability:{self.win_probability})>"