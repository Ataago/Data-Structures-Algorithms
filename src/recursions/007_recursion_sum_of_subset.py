# !/usr/bin/env python3
# encoding: utf-8

"""
    Given a list a list of Integers, find any subset which adds up to a Target.

    @author: Mohammed Ataaur Rahaman
"""


def sum_of_subset0(integers, target, subset):
    if sum(subset) == target:
        print(subset)
        exit(0)
    if len(integers) == 0:
        return

    sum_of_subset0(integers[1:], target, subset + [integers[0]])
    sum_of_subset0(integers[1:], target, subset)


if __name__ == '__main__':
    integers = [1, -10, 9, 4, 3, 2, 50, 12, 13, -5]
    target = 20

    sum_of_subset0(integers, target, [])
