#!/usr/bin/python3
"""
This script lists all states from the 'hbtn_0e_6_usa' database using SQLAlchemy

Arguments:
    mysql username
    mysql password
    database name
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    # Retrieve command-line arguments for the database connection
    db_user = sys.argv[1]      # MySQL username
    db_password = sys.argv[2]  # MySQL password
    db_name = sys.argv[3]      # Database name

    # Create a MySQL database connection using SQLAlchemy
    db_url = f'mysql+mysqldb://{db_user}:{db_password}@localhost/{db_name}'
    engine = create_engine(db_url, pool_pre_ping=True)

    # Create database tables if they don't exist
    Base.metadata.create_all(engine)

    # Create a database session
    session = Session(engine)

    # Retrieve and display the list of states from the 'State' table
    states = session.query(State).order_by(State.id).all()
    for state in states:
         print("{}: {}".format(state.id, state.name))

    # Close the database session to release resources
    session.close()
