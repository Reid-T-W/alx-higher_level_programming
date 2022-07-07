#!/usr/bin/python3
def weight_average(my_list=[]):
    if (len(my_list) == 0):
        return 0
    else:
        num_sum = 0
        denom_sum = 0
        for item in my_list:
            num_sum = num_sum + (item[0] * item[1])
            denom_sum = denom_sum + item[1]
        return (num_sum / denom_sum)
