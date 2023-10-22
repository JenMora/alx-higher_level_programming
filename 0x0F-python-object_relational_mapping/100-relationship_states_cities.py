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

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)

    # Create the State "California" and the City "San Francisco"
    # and associate them
    state  = State(name="California")
    city = City(name="San Francisco", state=state)

    session.add(state)
    session.add(city)

    session.commit()

    # Close the database session
    session.close()
