# !/usr/bin/env python3
# encoding: utf-8

"""
    Find the power of a given number.

    @author: Mohammed Ataaur Rahaman
"""


def power0(a, b, result):
    if not b:
        return print(result)

    power0(a, b - 1, result * a)


def power1(a, b):
    if not b:
        return 1

    return a * power1(a, b - 1)


def power2(a, b):
    if b == 1:
        return a

    half_pow = power2(a, int(b / 2))
    return half_pow * half_pow if b%2 == 0 else half_pow * half_pow * a


if __name__ == '__main__':
    a, b = map(int, input(f'Enter a and b for a^b: ').split(" "))
    power0(a, b, 1)

    pow = power1(a, b)
    print(pow)

    pow = power2(a, b)
    print(pow)
