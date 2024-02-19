#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel


class Place(BaseModel):
    """ A place to stay """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    # Task 9 updates
    # reviews = relationship('Review', back_populates='place',
    #                            cascade='all, delete-orphan')
    # @property
    # def reviews(self):
    #     """getter funtion to get reviews of certain place"""
    #     from models import storage
    #     reviews_dict = storage.all('Review')
    #     place_reviews = []
    #     for value in reviews_dict.values():
    #         if value.place_id == self.id:
    #             place_reviews.append(value)
    #     return place_reviews
