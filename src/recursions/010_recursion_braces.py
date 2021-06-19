# !/usr/bin/env python3
# encoding: utf-8

"""
    Find all the well-formed combinations of N {}.

    @author: Mohammed Ataaur Rahaman
"""


def permutations0(open_braces, close_braces, permutation):
    if not open_braces and not close_braces:
        return print(permutation)

    if open_braces:
        permutations0(open_braces - 1, close_braces, permutation + "{")
    if close_braces and open_braces < close_braces :
        permutations0(open_braces, close_braces - 1, permutation + "}")


def permutations1(open_braces, close_braces, permutation):
    if not open_braces and not close_braces:
        return [permutation]

    permutations = []
    if open_braces:
        permutations += permutations1(open_braces - 1, close_braces, permutation + "{")
    if close_braces and open_braces < close_braces :
        permutations += permutations1(open_braces, close_braces - 1, permutation + "}")

    return permutations


if __name__ == '__main__':
    n = int(input(f'Enter N: '))
    open_braces = close_braces = n
    permutations0(open_braces, close_braces, '')


    perm = permutations1(open_braces, close_braces, '')
    print(perm)
