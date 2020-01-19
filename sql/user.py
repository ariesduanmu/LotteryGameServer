# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2019-12-12 18:10:51
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-01-19 11:28:52
from datetime import datetime

from sql import Base

from sqlalchemy import Column
from sqlalchemy import VARCHAR
from sqlalchemy import Integer
from sqlalchemy import DateTime


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(VARCHAR(collation="utf8_unicode_ci", length=100), comment='联系人')
    did_lottery = Column(Integer, default=0, comment='已抽奖次数')
    create_timestamp = Column(DateTime(timezone=True), comment='创建的时间戳')
    lastlogin_timestamp = Column(DateTime(timezone=True), comment='最后登录的时间戳')

    def __init__(self, username):
        self.username = username
        
        current_timestamp = datetime.now()

        self.create_timestamp = current_timestamp
        self.lastlogin_timestamp = current_timestamp

    def lotter(self):
        self.did_lottery += 1

    def recent_login(self):
        self.lastlogin_timestamp = datetime.now()

    def __repr__(self):
        return f"<User(uuid:{self.uuid})>"