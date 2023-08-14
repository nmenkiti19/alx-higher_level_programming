#!/usr/bin/python3
def no_c(my_string):
    res = [lt for lt in my_string if lt != 'c' and lt != 'C']
    return ("".join(res))
