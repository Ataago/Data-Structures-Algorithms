# !/usr/bin/env python3
# encoding: utf-8

"""
    Find all the anagrams or permutations of a given word.

    @author: Mohammed Ataaur Rahaman
"""


def permutations0(word, anagram):
    if len(word) == 0:
        return print(anagram)

    for letter in word:
        permutations0(word.replace(letter, '', 1), anagram + letter)


if __name__ == '__main__':
    word = 'abc'
    permutations0(word, '')