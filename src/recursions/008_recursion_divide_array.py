# !/usr/bin/env python3
# encoding: utf-8

"""
    Given a list of integers, find if it is possible to divide it into two
    groups such that sum of one group is multiple of 5 and sum of the other is odd.

    @author: Mohammed Ataaur Rahaman
"""


def divide_array(array, group_1, group_2):
    if (len(array) == 0) and ((sum(group_1) % 5 == 0 and sum(group_2) % 2 == 1) or \
            (sum(group_2) % 5 == 0 and sum(group_1) % 2 == 1)):
        return print(f"Group 1: {group_1}\nGroup 2: {group_2}\n")
    if len(array) == 0:
        return

    divide_array(array[1:], group_1 + [array[0]], group_2)
    divide_array(array[1:], group_1, group_2 + [array[0]])

if __name__ == '__main__':
    array = [1, -10, 9, 4, 3, 2, 50, 12, 13, -5]
    divide_array(array, [], [])