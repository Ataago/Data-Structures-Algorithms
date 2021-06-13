# !/usr/bin/env python3
# encoding: utf-8

"""
    Basic Recursion Demo.

    @author: Mohammed Ataaur Rahaman
"""


def tail_rec(n):
    if n > 0:
        print(n, end=" ")
        tail_rec(n-1)


def head_rec(n):
    if n > 0:
        head_rec(n-1)
        print(n, end=" ")


def tree_rec(n):
    if n > 0:
        tree_rec(n-1)
        print(n, end=" ")
        tree_rec(n-1)


if __name__ == '__main__':
    n = int(input('Enter an Integer: '))

    print("\nTypes of Direct Recursions: ")
    # 3 2 1
    print("\nTail Recursion:")
    tail_rec(n)

    # 1 2 3
    print("\n\nHead Recursion:")
    head_rec(n)

    # 1 2 1 3 1 2 1
    print("\n\nTree Recursion:")
    tree_rec(n)
