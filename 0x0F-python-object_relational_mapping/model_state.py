#!/usr/bin/python3
"""
ORM Script
"""
import sys
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
            Column, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base

# Creating the engine
engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                       format(sys.argv[1], sys.argv[2], sys.argv[3]),
                       pool_pre_ping=True)
engine.connect()
Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)
