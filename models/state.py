#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship(
            "City",
            cascade='all,
            delete,
            delete-orphan',
            backref="state"
            )

    @property
    def cities(self):
        """
        returns the list of City instances with
        state_id equals to the current State.id
        """
        all_models = models.storage.all()
        semi = []
        final = []
        for key in all_models:
            city_class = key.split('.')
            if city_class[0] == 'City':
                semi.append(all_models[key])
        for item in semi:
            if item.state_id == self.id:
                final.append(items)
        return final
