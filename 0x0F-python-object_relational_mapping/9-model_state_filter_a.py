#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    db_username = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{db_username}:{db_password}@localhost/{db_name}')

    Session = sessionmaker(bind=engine)

    session = Session()
    like_state = session.query(State)\
        .filter(State.name.like('%a%'))\
        .order_by(State.id).all()
    for state in like_state:
        print(f'{state.id}: {state.name}')