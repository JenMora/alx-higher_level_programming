#!/usr/bin/python3
"""
A script that defines a State class and uses SQLAlchemy to
interact with a MySQL database.
The script creates a MySQL table called 'states' and allows
interaction with the 'State' class using SQLAlchemy.

Prerequisites:
- Make sure to install SQLAlchemy with 'pip install SQLAlchemy'.
- Replace 'username', 'password', and 'database_name' with your MySQL
- credentials and database name.
"""

# Import necessary modules from SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create the Base instance, which will be the base for all
# ORM class definitions
Base = declarative_base()


class State(Base):
    """
    Represents a state with a unique identifier and a name.

    Attributes:
        id (int): A unique identifier for the state.
        name (str): The name of the state.
    """
    # Specify the name of the MySQL table associated with this class
    __tablename__ = 'states'

    # Define class attributes that map to columns in the 'states' table

    id = Column(Integer, autoincrement=True, unique=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
