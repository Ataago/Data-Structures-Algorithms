# !/usr/bin/env python3
# encoding: utf-8

"""
    Tower of Hanoi

    @author: Mohammed Ataaur Rahaman
"""

def hanoi(n, src, tmp, dest):
    """
    Given elements in array. add if its even else subtract.
    """
    if n == 1:
        print(f"Move Disk {n} from '{src}' to '{dest}'.")
        return

    hanoi(n - 1, src=src, tmp=dest, dest=tmp)
    print(f"Move Disk {n} from '{src}' to '{dest}'.")
    hanoi(n - 1, src=tmp, tmp=src, dest=dest)


if __name__ == '__main__':
    n = int(input('Enter an Integer: '))
    hanoi(n=n, src='A', tmp='B', dest='C')
