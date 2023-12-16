#!/usr/bin/python3
'''
Module: 7. All states via SQLAlchemy
prints all objects from database
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

    '''
    this prints only the first row thanks to the slice
    for instance in session.query(State).order_by(State.id)[:1]:
        print('{}: {}'.format(instance.id, instance.name))
    '''
    # Query first row:
    instance = session.query(State).first()

    # condition to check that row is not empty
    if instance:
        print('{}: {}'.format(instance.id, instance.name))
    else:
        print('Nothing')

    session.close()
