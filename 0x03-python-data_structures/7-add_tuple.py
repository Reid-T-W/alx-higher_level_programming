#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = ()
    list_c = []
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    for i in range(2):
        sum_1 = 0
        if (i <= len_a - 1):
            sum_1 = sum_1 + tuple_a[i]
        elif (i > len_a - 1):
            sum_1 = sum_1 + 0
        if (i <= len_b - 1):
            sum_1 = sum_1 + tuple_b[i]
        elif(i > len_b - 1):
            sum_1 = sum_1 + 0
        list_c.append(sum_1)
    tuple_c = (list_c[0], list_c[1],)
    return tuple_c
