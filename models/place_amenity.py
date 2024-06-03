#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, Integer, Float, Table
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship


place_amenity = Table('lace_amenity', Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id', onupdate='CASCADE',
                                            ondelete='CASCADE'), primary_key=True, nullable=False),
        Column('amenity_id', String(60), ForeignKey('amenities.id', onupdate='CASCADE',
                                            ondelete='CASCADE'), primary_key=True, nullable=False)),
