#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set()
    sum = 0
    my_set = set(map(lambda x: x, my_list))
    for i in my_set:
        sum = sum + i
    return sum
