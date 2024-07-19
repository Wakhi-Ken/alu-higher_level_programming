#!/usr/bin/python3
"""Student class."""


class Student:
    """A class with  first_name, last_name, and age attributes."""
    def __init__(self, first_name, last_name, age):
        """Initializes public attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary representation of the instance"""
        my_dict = {}
        if isinstance(attrs, list):
            for name in attrs:
                if isinstance(name, str) and name in self.__dict__:
                    my_dict[name] = self.__dict__[name]
            return my_dict
        return self.__dict__
