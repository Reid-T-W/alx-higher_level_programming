#!/usr/bin/python3
'''This moudle inherits from list'''


class MyList(list):
    '''This class extends from list, it prints a sorted list'''
    def print_sorted(self):
        '''This function prints a sorted copy of the original list'''
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
