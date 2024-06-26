#!/usr/bin/python3
"""
prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    db_username = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    searched_obj = sys.argv[4]

    engine = create_engine(
        f'mysql+mysqldb://{db_username}:{db_password}@localhost/{db_name}')

    Session = sessionmaker(bind=engine)

    session = Session()
    query_obj = session.query(State)\
        .filter(State.name == searched_obj).all()

    if query_obj:
        for item in query_obj:
            print(item.id)
    else:
        print("Not found")