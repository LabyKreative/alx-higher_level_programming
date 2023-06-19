#!/usr/bin/python3
"""
a script 14-model_city_fetch_by_state.py that prints all City
objects from the database hbtn_0e_14_usa:
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == '__main__':
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State, City).filter(State.id == City.state_id).all()

    for state, city in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
