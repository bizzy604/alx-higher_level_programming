#!/usr/bin/python3
"""
class definition of a State and an instance Base = declarative_base()
"""
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine

Base = declarative_base()


class State(Base):
    """
    State class representing 'state' table in data base
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        """
        Initializing object
        """
        self.name = name


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2],
            sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)