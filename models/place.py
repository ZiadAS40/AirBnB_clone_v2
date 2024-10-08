#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_ident
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime


if storage_ident == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
            Column('place_id',
                    String(60),
                      ForeignKey('places.id'),
                        primary_key=True,
                          nullable=False),
            Column('amenity_id',
                    String(60),
                      ForeignKey('amenities.id'),
                        primary_key=True,
                          nullable=False))


class Place(BaseModel, Base if storage_ident == 'db' else object):
    """ A place to stay """

    if storage_ident == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', backref='place')
        amenities = relationship("Amenity", secondary="place_amenity",
                                 backref="place_amenities",
                                 viewonly=False)

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
    
    if storage_ident != 'db':
        @property
        def reviews(self):
            """
            return a list of reviews instances
            if the current 'place.id == obj.id'
            """
            from models import storage
            re_obj = storage.all("Review")
            final_list = []
            for  v in re_obj.values():
                if self.id == v.place_id[1:-1]:
                    final_list.append(v)
            return final_list
        
        @property
        def amenities(self):
            """
            return a list of amenities instances
            if the current 'place.id == obj.id'
            """
            from models import storage
            re_obj = storage.all("Amenity")
            final_list = []
            for v in re_obj.values():
                if self.id == v.amenity_id[1:-1]:
                    final_list.append(v)
            return final_list
           