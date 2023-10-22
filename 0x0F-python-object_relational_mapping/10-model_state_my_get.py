#!/usr/bin/python3
"""
Prints the first State object from the 'hbtn_0e_6_usa' database
arguments:
    mysql username
    mysql password
    database name
    state name to search
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Get the command-line arguments
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Create a MySQL database connection
    db_ur = f'mysql+mysqldb://{db_user}:{db_password}@localhost:3306/{db_name}'
    engine = create_engine(db_ur, pool_pre_ping=True)

    # Create a database session
    session = Session(engine)

    # Query for state with specified name
    result = session.query(State).filter(State.name == state_name).first()

    if result:
        print(result.id)
    else:
        print("Not found")

    # Close the database session
    session.close()
