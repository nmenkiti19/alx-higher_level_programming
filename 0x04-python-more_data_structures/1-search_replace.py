#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nu_list = my_list.copy()
    for i in range(len(nu_list)):
        nu_list[i] = replace if my_list[i] == search else my_list[i]
    return (nu_list)
