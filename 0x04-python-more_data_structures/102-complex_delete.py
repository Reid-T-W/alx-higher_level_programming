#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    copy_dict = a_dictionary.copy()
    if (value in copy_dict.values()):
        for key, val in copy_dict.items():
            if (val == value):
                del a_dictionary[key]
        return a_dictionary
    else:
        return a_dictionary
