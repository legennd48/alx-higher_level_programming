#!/usr/bin/python3
"""
Module: 17. From city
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(State).order_by(State.id).all()
    for instance in rows:
        for cityI in instance.cities:
            print(cityI.id, cityI.name, sep=": ", end="")
            print(" -> " + instance.name)

    session.close()
