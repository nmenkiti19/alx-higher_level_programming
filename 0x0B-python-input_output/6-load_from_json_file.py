#!/usr/bin/python3
# 6-load_from_json_file.py
"""Creates object from JSON"""
import json


def load_from_json_file(filename):
    """Creates object from JSON file"""
    with open(filename) as fyl:
        return json.load(fyl)
