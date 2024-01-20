#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    # state_id = ""
    # name = ""

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id", ondelete='CASCADE'),
                      nullable=False)

    places = relationship(
        'models.place.Place',  # or just 'Place'
        backref='cities',
        cascade='all, delete-orphan')
