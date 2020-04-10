# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2019-12-12 18:09:03
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-10 12:34:08
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///lottery.sqlite')

Base = declarative_base()

metadata = Base.metadata

session = sessionmaker()
session.configure(bind=engine)


