#!/usr/bin/python3
# 100-append_after.py
"""function appends stuff"""


def append_after(filename="", search_string="", new_string=""):
    """Adds text after each line """
    xter = ""
    with open(filename) as fyl:
        for lyn in fyl:
            xter += lyn
            if search_string in lyn:
                xter += new_string
    with open(filename, "w") as w:
        w.write(xter)
