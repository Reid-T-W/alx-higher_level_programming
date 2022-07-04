#!/usr/bin/python3
def multiple_returns(sentence):
    len_sen = len(sentence)
    tup = ()
    if len_sen != 0:
        first_let = sentence[0]
        tup = (len_sen, first_let,)
    elif len_sen == 0:
        tup = (len_sen, "None",)
    return tup
