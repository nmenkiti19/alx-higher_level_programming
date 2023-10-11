#!/usr/bin/python3
# 10-student.py
"""This is a Student class"""

class Student:
    """Represents 1 student"""

    def __init__(self, first_name, last_name, age):
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets a dictionary rep of Student

        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {ind: getattr(self, ind) for ind in attrs if hasattr(self, ind)}
        return self.__dict__
