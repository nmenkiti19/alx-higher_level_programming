#!/usr/bin/python3
# 1-number_of_lines.py
def number_of_lines(filename=""):
    """writes string to text file"""
    lynz = 0
    with open(filename) as fyl:
        for line in fyl:
            lynz += 1
    return lynz
