#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

try:
    if os.environ["HBNB_TYPE_STORAGE"] == "db":
        from models.engine.db_storage import DBStorage
        storage = DBStorage()
        storage.reload()
except:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
