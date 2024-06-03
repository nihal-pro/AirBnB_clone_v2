#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv

STORAGE_TYPE = getenv("HBNB_TYPE _STORAGE")

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    if STORAGE_TYPE != "db":
        @property
        def cities(self):
            """ relationship between State and City """
            from models.__init__ import storage
            cities = []
            for ct in storage.all(City).values():
                if self.id == ct.state_id:
                    cities.append(ct)
            return cities
        