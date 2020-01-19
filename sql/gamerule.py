# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2019-12-25 10:34:21
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-01-19 13:23:27
from sql import Base

from sqlalchemy import Column
from sqlalchemy import Integer



class GameRule(Base):
    __tablename__ = 'game_rule'
    id = Column(Integer, primary_key=True, autoincrement=True)
    win_probability = Column(Integer, default=20, comment='获奖的概率')
    max_lottery = Column(Integer, default=5, comment='最大抽奖次数')

    def __repr__(self):
        return f"<GameRule(max_lottery:{self.max_lottery})>"