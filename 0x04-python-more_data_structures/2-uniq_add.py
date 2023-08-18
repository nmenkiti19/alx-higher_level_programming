#!/usr/bin/python3
def uniq_add(my_list=[]):
    st = 0
    for i in set(my_list):
        st += i
    return (st)
