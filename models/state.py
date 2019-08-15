#!/usr/bin/python3
"""This is the state class"""
import models
import os
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

    try:
        if os.environ["HBNB_TYPE_STORAGE"] == "db":
            cities = relationship("City", cascade="save-update, merge, delete",
                                  backref="state")
    except:
        @property
        def cities(self):
            """list all cities with relationship
            """
            for key, value in models.storage.all(City).items():
                if self.id == value.state_id:
                    cities.append(value)
