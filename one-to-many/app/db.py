import os
import sys

sys.path.append(os.getcwd)

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///one_to_many.db')

Base = declarative_base()

class Game(Base):
    __tablename__ = 'games'

    game_id = Column(Integer(), primary_key=True)
    game_title = Column(String())
    game_genre = Column(String())
    game_platform = Column(String())
    game_price = Column(Integer())
