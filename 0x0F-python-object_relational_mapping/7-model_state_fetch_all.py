#!/usr/bin/python3
"""
Lists all State objects from the hbtn_0e_6_usa database.

This script connects to a MySQL database using SQLAlchemy and retrieves all State objects
from the 'states' table. The retrieved State objects are then printed in the format 'id: name'.

Usage:
    python3 script.py <username> <password> <database>

Arguments:
    <username>: The username to connect to the MySQL database.
    <password>: The password for the MySQL user.
    <database>: The name of the database containing the 'states' table.

Example:
    python3 script.py root password hbtn_0e_6_usa
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

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
