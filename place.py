#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_ident
from sqlalchemy import Column, String, ForeignKey, Integer, Float


class Place(BaseModel, Base if storage_ident == 'db' else object):
    """ A place to stay """
    if storage_ident == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities_id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users_id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, nullable=False)
        number_bathrooms = Column(Integer, nullable=False, nullable=False)
        max_guest = Column(Integer, nullable=False, nullable=False)
        price_by_night = Column(Integer, nullable=False, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
    else:
        user_id = ""
        city_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
    
    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)
