#!/usr/bin/python3
"""
City class
inherits from Base (imported from model_state)
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """
    links to the MySQL table cities
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False)
    state = relationship(State)