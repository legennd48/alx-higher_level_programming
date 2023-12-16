#!/usr/bin/python3
'''
Module 12. Update a state
deletes all State objects with a name containing the
letter a from the database
'''
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    user = argv[1]
    pw = argv[2]
    dbName = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           user, pw, dbName, pool_pre_ping=True))
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(State).filter(State.name.like('%a%')).delete()

    session.commit()

    session.close()
