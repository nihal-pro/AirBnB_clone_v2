#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, Integer, Float, Table
from sqlalchemy.sql.schema import ForeignKey
from models.review import Review
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from sqlalchemy.ext.declarative import declarative_base
from models.city import City
from models.user import User

Base = declarative_base()
place_amenity = Table('lace_amenity', Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id', onupdate='CASCADE',
                                            ondelete='CASCADE'), primary_key=True, nullable=False),
        Column('amenity_id', String(60), ForeignKey('amenities.id', onupdate='CASCADE',
                                            ondelete='CASCADE'), primary_key=True, nullable=False),
)
class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude =  Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    
    reviews = relationship("City", backref="place", cascade="all, delete")
    amenities = relationship('Amenity', secondary="place_amenity",
                                 back_populates="place_amenities",
                                 viewonly=False)

    @property
    def reviews(self):
        """ relationship between review and Place """
        from models.__init__ import storage
        reviews = []
        for rev in storage.all(Review).values():
            if self.id == rev.place_id:
                reviews.append(rev)
        return reviews

    @property
    def amenities(self):
        """ relationship between Amenity and Place """
        from models.__init__ import storage
        amenities = []
        for amen in storage.all(Amenity).values():
            if self.id == amen.place_id:
                amenities.append(rev)
        return reviews
    @amenities.setter
    def amenities(self, Amenity):
        """ set amenities """
        if isinstance(amenity, Amenity):
            self.amenity_ids.append(amenity.id)
    
        
    

