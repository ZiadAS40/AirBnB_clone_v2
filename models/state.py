#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.engine.file_storage import FileStorage
from os import getenv


class State(BaseModel, Base):
    """ State class """
    if getenv('HBNB_TYPE_STORAGE') == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""
    
    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
    
    @property
    def cities(self):
        """
        return all the cities with
        the current state_id
        """
        myList = []
        for key, value in FileStorage.__objects.items():
            if key.split('.')[0] == "City":
                if value.state_id == self.id:
                    myList.append(value)
        
        return myList
