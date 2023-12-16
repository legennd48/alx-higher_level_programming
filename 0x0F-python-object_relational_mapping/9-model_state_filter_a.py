#!/usr/bin/python3
'''
Module: 9. Contains `a`
lists all State objects that contain the letter a from the database
'''

from model_state import Base, State
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    user = argv[1]
    pw = argv[2]
    dbName = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           user, pw, dbName, pool_pre_ping=True))
    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).filter(
            State.name.like('%a%')).order_by(State.id):
        print('{}: {}'.format(instance.id, instance.name))

    session.close()
