#!/usr/bin/python3
# 5-save_to_json_file.py
"""Save object to file using JSON."""
import json

def save_to_json_file(my_obj, filename):
    """save an object to file using JSON"""
    with open(filename, "w") as fyl:
        json.dump(my_obj, fyl)
