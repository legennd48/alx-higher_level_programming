#!/usr/bin/python3
'''
Module 12. Update a state
 changes the name of a State object from the database
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

    instance = session.query(State).filter_by(id=2).first()
    instance.name = 'New Mexico'

    session.commit()

    session.close()
