#!/usr/bin/python3
"""
create state "California" with city attribute "San Francisco"
parameters given to script: username, password, database
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    user = argv[1]
    passwd = argv[2]
    dbName = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(user, passwd, dbName), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # create state "California" with city attribute "San Francisco"
    newState = State(name="California")
    newCity = City(name="San Francisco")
    newState.cities.append(newCity)

    session.add(newState)
    session.add(newCity)

    session.commit()
    session.close()
