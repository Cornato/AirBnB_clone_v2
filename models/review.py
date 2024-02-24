#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel):
    """ Review classto store review information """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    user = relationship("User", cascade="all,delete", back_populates="review")
    place = relationship("Place", cascade="all,delete", back_populates="review")
