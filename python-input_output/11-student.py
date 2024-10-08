#!/usr/bin/python3
"""Student class"""


class Student:
    """A class with a first_name, last_name, and age attributes"""
    def __init__(self, first_name, last_name, age):
        """Initializes public attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets the dictionary representation of the instance"""
        my_dict = {}
        if isinstance(attrs, list):
            for name in attrs:
                if isinstance(name, str) and name in self.__dict__:
                    my_dict[name] = self.__dict__[name]
            return my_dict
        return self.__dict__

    def reload_from_json(self, json):
        """Sets attributes of an instance"""
        for key in json:
            setattr(self, key, json[key])
