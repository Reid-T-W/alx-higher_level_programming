#!/usr/bin/python3
"""
ORM Script
"""
import sys
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
            Column, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base, State


class City(Base):
    """
    Creates the City class
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
