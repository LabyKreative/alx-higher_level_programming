#!/usr/bin/python3
"""
a script that changes the name of a State object from the
database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    updateState = session.query(State).filter(State.id == 2).first()

    if updateState:
        updateState.name = 'New Mexico'
        session.commit()
