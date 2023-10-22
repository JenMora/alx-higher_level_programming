#!/usr/bin/python3
"""
Module for the State class definition
with relationship to City.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class definition, inherits from Base.
    Represents a table 'states' with columns id,
    name, and a relationship to City.
    """
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, unique=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
    rel = relationship
    cities = rel("City", backref="state", cascade="all, delete-orphan")
