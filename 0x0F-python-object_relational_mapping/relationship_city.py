#!/usr/bin/python3
'''
class definition of city
'''
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    '''
    definitition of class with id, name and f+key attributes
    '''
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
