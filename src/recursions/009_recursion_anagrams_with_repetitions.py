# !/usr/bin/env python3
# encoding: utf-8

"""
    Find all the anagrams or permutations of n abc.

    @author: Mohammed Ataaur Rahaman
"""


def permutations0(a_nos, b_nos, c_nos, permutation):
    if not a_nos and not b_nos and not c_nos:
        return print(permutation)

    if a_nos:
        permutations0(a_nos - 1, b_nos, c_nos, permutation + 'a')
    if b_nos:
        permutations0(a_nos, b_nos - 1, c_nos, permutation + 'b')
    if c_nos:
        permutations0(a_nos, b_nos, c_nos - 1, permutation + 'c')


if __name__ == '__main__':
    n = int(input(f'Enter N: '))
    a_nos = b_nos = c_nos = n
    permutations0(a_nos, b_nos, c_nos, '')