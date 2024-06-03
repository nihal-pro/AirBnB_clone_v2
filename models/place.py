#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, Integer, Float, Table
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from models.place_amenity import place_amenity
from models.amenity import Amenity


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
    place_amenities = relationship("Place", secondary=place_amenity, viewonly=False)
    class Amenity(BaseModel, Base):
        """ Amenity class """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)


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
                amenities.append(amen)
        return reviews
    @amenities.setter
    def amenities(self, Amenity):
        """ set amenities """
        if isinstance(amenity, Amenity):
            self.amenity_ids.append(amenity.id)
    
    
        
    

