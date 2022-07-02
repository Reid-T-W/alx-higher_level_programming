#!/usr/bin/python3
def no_c(my_string):
    no_c_my_string = ""
    for i in range(len(my_string)):
        if (my_string[i] != 'c' and my_string[i] != 'C'):
            no_c_my_string = no_c_my_string + my_string[i]
    return no_c_my_string
