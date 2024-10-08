#!/usr/bin/python3
""" define the state class"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from datetime import datetime
from sqlalchemy import Column, String, DATETIME
from sqlalchemy.orm import relationship
from models import storage_ident


class State(BaseModel, Base if storage_ident == "db" else object):
    """class state """
    if storage_ident == "db":
        __tablename__ = 'states'
        id = Column(String(60), primary_key=True)
        created_at = Column(DATETIME, default=datetime.utcnow())
        updated_at = Column(DATETIME,
                        nullable=False,
                        default=datetime.utcnow())
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if storage_ident != "db":
        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
