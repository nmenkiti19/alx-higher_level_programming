#!/usr/bin/python3
def no_c(my_string):
    result = [letter for letter in my_string if letter != 'c' and letter != 'C']
    return ("".join(result))
