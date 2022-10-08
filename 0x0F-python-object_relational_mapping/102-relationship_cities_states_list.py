#!/usr/bin/python3
"""
Module that adds a state to the states table
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    all_cities = session.query(City).all()
    for city in all_cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
