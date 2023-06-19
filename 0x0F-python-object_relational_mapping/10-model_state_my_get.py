#!/usr/bin/python3
"""
a script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    username, password, database, searched_state = sys.argv[
        1], sys.argv[2], sys.argv[3], sys.argv[4]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == searched_state).first()

    print("Not found" if not state else state.id)
