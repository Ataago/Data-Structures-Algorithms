# !/usr/bin/env python3
# encoding: utf-8

"""
    Find all the subset of letters given a word.

    Solution: Binary recursive calls by enriching solution.

                       word,
                      subset
                        /\
              (in)    /    \    (out)
                    /        \
            word[1:],         word[1:],
    subset + word[0]          subset


    @author: Mohammed Ataaur Rahaman
"""

import time

def combinations0(word, subset):
    if len(word) == 0:
        return print(f"'{subset}',", end=" ")

    combinations0(word[1:], subset + word[0])
    combinations0(word[1:], subset)


def combinations1(word, subset):
    if len(word) == 0:
        return {subset}

    a = combinations1(word[1:], subset + word[0])
    b = combinations1(word[1:], subset)
    return a.union(b)


def combinations2(word, subset):
    if len(word) == 0:
        return [subset]

    a = combinations2(word[1:], subset + word[0])
    b = combinations2(word[1:], subset)
    return a + b


if __name__ == '__main__':
    word = str(input("Enter a word: "))

    # Outputing in recursive call
    start = time.time()
    print("\nRecursion type 1: ", end="")
    combinations0(word, '')
    print(f"\nTime taken I: {time.time() - start}")

    # Recursive call returns
    start = time.time()
    subsets = combinations1(word, '')
    print(f"\nRecursion type 2: {subsets}")
    print(f"Time taken II: {time.time() - start}")

    # Recursive call returns list
    start = time.time()
    subsets = combinations2(word, '')
    print(f"\nRecursion type 3: {subsets}")
    print(f"Time taken III: {time.time() - start}")
