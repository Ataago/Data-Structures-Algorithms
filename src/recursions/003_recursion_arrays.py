# !/usr/bin/env python3
# encoding: utf-8

"""
    Array problems

    @author: Mohammed Ataaur Rahaman
"""

def problem0(array):
    """
    Given elements in array. add if its even else subtract.
    """
    if len(array) == 0:
        return 0

    if array[0]% 2 == 0:
        return problem0(array[1:]) + array[0]
    else:
        return problem0(array[1:]) - array[0]

if __name__ == '__main__':

    array = [1, 2, 3, 10, 7, 8]
    print(problem0(array))