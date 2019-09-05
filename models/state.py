#!/usr/bin/python3
"""This is the state class"""
import models
from os import getenv
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
            cities = relationship("City", cascade="save-update, merge, delete",
                                  backref="state")
    else:
        @property
        def cities(self):
            """return list all cities with relationship
            """
            cities = []
            for key, value in models.storage.all(City).items():
                if self.id == value.state_id:
                    cities.append(value)
            return(cities)
