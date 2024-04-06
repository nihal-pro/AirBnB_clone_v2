#!/usr/bin/python3
"""This module defines a class to manage DB storage SQLalchemy"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user import User
from models.state import State 
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import scoped_session
from models.base_model import Base

class DBStorage:
    """Create class dbdtorage"""
    __engine = None
    __session = None
    
    
    def __init__(self):
        """ create engine """
        User = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db_name = os.getenv("HBNB_MYSQL_DB")
    
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(User, password, db_name), pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
        
    def all(self, cls=None):
        """ query on the current database session """
        __dic = {}
        if cls:
            classes = self.__session.query(cls).all()
            for obj in classes:
                key = f"{obj.__class__.__name__}.{obj.id}" #cls.name = obj.__class__.__name__
                __dic[key] = obj
            return __dic
        else:
            for cl in [User, State, City]:
                classes = self.__session.query(cl).all()
                for obj in classes:
                    key = f"{obj.__class__.__name__}.{obj.id}" #cls.name = obj.__class__.__name__
                    __dic[key] = obj
            return __dic
                
    def new(self, obj):
        """ add object"""
        if obj:
            self.__session.add(obj)
    def save(self):
        """ save all"""
        self.__session.commit()
    
    def delete(self, obj=None):
        """ delete object"""
        if obj:
            self.__session.delete(obj)
    
    def reload(self):
        """ create all tables in the database """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit = False)
        Session = scoped_session(session_factory)
        self.__session = Session()
    
    def close(self):
        """ close session """
        self.__session.close()
        
        
    
        
