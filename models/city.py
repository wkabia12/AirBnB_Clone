#!/usr/bin/python3
"""
    Class City that inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ City class inheriting from BaseModel """
    state_id = ""
    name = ""
