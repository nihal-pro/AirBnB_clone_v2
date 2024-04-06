#!/usr/bin/python3
"""This module instantiates an object of class FileStorage and DBStorage"""
from os import getenv



is_equal = (getenv("HBNB_TYPE_STORAGE") == "db")
if is_equal:
    from models.engine.db_storage import DBStorage
    storage =  DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
    
