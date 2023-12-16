#!/usr/bin/python3
'''
Module 11. Add a new state
adds the State object “Louisiana” to the database
'''
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    user = argv[1]
    pw = argv[2]
    dbName = argv[3]
    newState = State(name='Louisiana')

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           user, pw, dbName, pool_pre_ping=True))
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(newState)
    session.commit()

    instance = session.query(State).filter_by(name='Louisiana').first()
    print('{}'.format(instance.id))

    session.close()
