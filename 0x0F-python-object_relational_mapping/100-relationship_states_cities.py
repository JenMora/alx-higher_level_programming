#!/usr/bin/python3
"""
Creates the State “California” with the City “San Francisco” in the
database hbtn_0e_100_usa.
"""

import sys
from relationship_city import City
from relationship_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    # Get the command-line arguments
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

    # Create a MySQL database connection
    db_ur = f'mysql+mysqldb://{db_user}:{db_password}@localhost:3306/{db_name}'
    engine = create_engine(db_ur, pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)

    # Create the State "California" and the City "San Francisco"
    # and associate them
    california = State(name="California")
    san_francisco = City(name="San Francisco")

    california.cities.append(san_francisco)
    session.add(california)

    session.commit()

    # Close the database session
    session.close()
