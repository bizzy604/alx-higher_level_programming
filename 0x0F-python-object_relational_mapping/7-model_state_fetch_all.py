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
    all_states = session.query(State).all()
    for item in all_states:
        print(f'{item.id}: {item.name}')