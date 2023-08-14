#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_multiples = list(my_list)
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            list_multiples[i] = True
        else:
            list_multiples[i] = False
    return list_multiples
