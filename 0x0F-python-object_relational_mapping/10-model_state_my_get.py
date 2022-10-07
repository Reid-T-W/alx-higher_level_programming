#!/usr/bin/python3
"""
Module that retrieves id of states searched by user
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    states = session.query(State).filter(State.name == sys.argv[4]).first()
    if states is None:
        print("Not found")
    else:
        print("{}".format(states.id))
