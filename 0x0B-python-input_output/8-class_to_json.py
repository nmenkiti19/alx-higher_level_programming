#!/usr/bin/python3
# 8-class_to_json.py
"""Class-to-JSON function"""

def class_to_json(obj):
    """Returns dictionary representation of a simple DS"""
    return obj.__dict__
