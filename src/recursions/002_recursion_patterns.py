# !/usr/bin/env python3
# encoding: utf-8

"""
    Pattern printing

    @author: Mohammed Ataaur Rahaman
"""


def pyramid0(n):
    """
    To print:
        *
        * *
        * * *
        * * * *
        * * * * *
    """
    if n > 0:
        pyramid0(n-1)
        print('* '*n)

def pyramid1(n, total):
    """
    To print:
                *
              * *
            * * *
          * * * *
        * * * * *
    """
    if n > 0:
        print('  '*(n-1), end='')
        print('* '*(total - n+1))
        pyramid1(n-1, total)


def pyramid2(n, total):
    """
    To print:
            *
           * *
          * * *
         * * * *
        * * * * *
    """
    if n > 0:
        print(' '*(n), end='')
        print('* '*(total - n+1))
        pyramid2(n-1, total)


def pyramid3(n, char):
    """
    To print:
        A
        A B
        A B C
        A B C D
        A B C D E
    """
    if n > 0:
        pyramid3(n-1, char)
        print("".join([chr(idx) + " " for idx in range(ord(char), ord(char) + n, 1)]))


if __name__ == '__main__':
    n = int(input('Enter an Integer: '))

    print("\nPrinting pyramid 0:")
    pyramid0(n)

    print("\nPrinting pyramid 1:")
    pyramid1(n, n)

    print("\nPrinting pyramid 2:")
    pyramid2(n, n)

    print("\nPrinting pyramid 3:")
    pyramid3(n, 'A')
