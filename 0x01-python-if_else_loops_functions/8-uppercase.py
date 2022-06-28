#!/usr/bin/python3
def uppercase(str):
    uc_str = ""
    for char in str:
        lc_l = ord(char)
        if (lc_l >= 97 and lc_l <= 122):
            lc_l = lc_l - 32
        print("{:c}".format(lc_l), end="")
    print()
