#!/usr/bin/python3
def number_keys(a_dictionary):
    nb = 0
    list_keys = list(a_dictionary.keys())

    for x in list_keys:
        nb += 1

    return (nb)
