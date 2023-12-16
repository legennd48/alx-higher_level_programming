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
    find = argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           user, pw, dbName, pool_pre_ping=True))
    Session = sessionmaker(bind=engine)
    session = Session()

    instance = session.query(State).filter(
        State.name.like('%{}%'.format(find))).first()
    if instance:
        print('{}'.format(instance.id))
    else:
        print('Not found')

    session.close()
