#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_ident
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship



class Amenity(BaseModel, Base if storage_ident == 'db' else object):
    """the Amenity Class"""
    if storage_ident == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""
