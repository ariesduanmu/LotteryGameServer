# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2019-12-12 18:11:12
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-01-19 11:03:44
from datetime import datetime

from sql import Base

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime


class Lottery(Base):
    __tablename__ = 'lottery'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), comment='抽奖用户的id')
    create_timestamp = Column(DateTime(timezone=True), comment='创建的时间戳')

    def __init__(self, user_id):
        self.user_id = user_id
        self.create_timestamp = datetime.now()

    def __repr__(self):
        return f"<Lottery(user_id:{self.user_id})>"