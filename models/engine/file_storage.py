#!/usr/bin/python3
"""
    Module to (De)Serialize python objects to/from json
"""


import json


class FileStorage():
    """
        Class to (De)Serialize python objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return dict of all objects """
        self.reload()
        return FileStorage.__objects

    def new(self, obj):
        """ adds to __objects the object with key as object class name.id"""
        self.reload()
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """ save __objects dict to json file """
        with open(FileStorage.__file_path, mode="w", encoding='utf-8') as file:
            json.dump(FileStorage.__objects, file)
        FileStorage.__objects = {}

    def reload(self):
        """ loads json object from file """
        try:
            with open(FileStorage.__file_path, mode="r",
                      encoding="utf-8") as file:
                FileStorage.__objects = json.load(file)
        except IOError:
            pass
