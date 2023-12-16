#!/usr/bin/python3
'''
prints all City objects from the database
'''
from model_state import Base, State
from model_city import City
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    userName = argv[1]
    pw = argv[2]
    dbName = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           userName, pw, dbName, pool_pre_ping=True))
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State.name, City.id, City.name).filter(
                           State.id == City.state_id).order_by(City.id)
    for instance in result:
        print("{}: ({}) {}".format(instance[0], instance[1], instance[2]))
