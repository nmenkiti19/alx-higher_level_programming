#!/usr/bin/python3
# 2-read_lines.py
def append_write(filename="", text=""):
    """appends string to end of a text file
    returns no of characters appended"""
    with open(filename, mode='a', encoding='utf-8') as fyl:
        return fyl.write(text)
