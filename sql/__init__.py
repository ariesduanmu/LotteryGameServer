# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2019-12-12 18:09:03
# @Last Modified by:   Li Qin
# @Last Modified time: 2019-12-25 10:57:49
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config.database import DB_USERNAME
from config.database import DB_PASSWORD
from config.database import DB_DATABASE

engine = create_engine(f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@localhost/{DB_DATABASE}?charset=utf8')

Base = declarative_base()

session = sessionmaker()
session.configure(bind=engine)

