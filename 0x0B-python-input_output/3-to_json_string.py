#!/usr/bin/python3
'''# 3-to_json_string.py'''

import json

def to_json_string(my_obj):
    """returns JSON rep
    of object"""
    js = json.dumps(my_obj)
    return js
