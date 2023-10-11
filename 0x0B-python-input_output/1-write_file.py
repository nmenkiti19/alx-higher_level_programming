#!/usr/bin/python3
# 1-write_file.py
"""writes to file."""


def write_file(filename="", text=""):
    """Writes to a text file
        returns no of xters written
    """
    with open(filename, "w", encoding="utf-8") as fyl:
        return fyl.write(text)
