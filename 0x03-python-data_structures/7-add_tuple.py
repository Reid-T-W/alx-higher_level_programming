#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = ()
    list_c = []
    sum_1 = 0
    for i in range(2):
        if (not tuple_a[i]):
            sum_1 = sum_1 + 0
        elif (tuple_a[i]):
            sum_1 = sum_1 + tuple_a[i]
        if (not tuple_b[i]):
            sum_1 = sum_1 + 0
        elif (tuple_b[i]):
            sum_1 = sum_1 + tuple_b[i]
        list_c.append(sum_1)
    tuple_c = (list_c[0], list_c[1],) 
    return tuple_c
        
