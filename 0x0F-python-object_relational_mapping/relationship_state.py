#!/usr/bin/python3
"""
Contains the class definition for State model
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


metadata = MetaData()
Base = declarative_base(metadata=metadata)


class State(Base):
    """
    Represents and defines each state
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")
