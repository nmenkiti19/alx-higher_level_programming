#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    int_g = my_list[0]
    for indx in range(len(my_list)):
        if my_list[indx] > int_g:
            int_g = my_list[indx]

    return (int_g)
