#!/usr/bin/python3
"""checks if an object is an instance of class or of a class it inherited from"""
def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    return False
