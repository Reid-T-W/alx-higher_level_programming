#!/usr/bin/python3
"""
Module that adds a state to the states table
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    cities = session.query(City).all()
    for city in cities:
        state = session.query(State).filter(city.state_id == State.id).first()
        print("{}: ({}) {}".format(state.name, city.id, city.name))
