#!/usr/bin/python3
"""
Prints the first State object from the 'hbtn_0e_6_usa' database
arguments:
    mysql username
    mysql password
    database name
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Get the command-line arguments
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

    # Create a MySQL database connection
    db_ur = f'mysql+mysqldb://{db_user}:{db_password}@localhost:3306/{db_name}'
    engine = create_engine(db_ur, pool_pre_ping=True)

    # Create a database session
    session = Session(engine)

    # Query for City objects from the database and print the results
    ses = session.query

    cities = ses(City).order_by(City.id).all()
    for city in cities:
        state_name = ses(State.name).filter(State.id == city.state_id).scalar()
        print(f"{state_name}: ({city.id}) {city.name}")

    # Close the database session
    session.close()
