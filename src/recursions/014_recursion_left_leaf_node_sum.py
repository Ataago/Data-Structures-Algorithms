# !/usr/bin/env python3
# encoding: utf-8

"""
    Sum of all leaf nodes that are to the left of its parent in a tree.

    @author: Mohammed Ataaur Rahaman
"""


class Node:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def sum_of_left_leaf_nodes(node, is_left=False):

    if is_left and node.left is None:
        return node.data

    if not node.right:
        return 0

    l = sum_of_left_leaf_nodes(node.left, True)
    r = sum_of_left_leaf_nodes(node.right, False)

    return l + r

if __name__ == '__main__':
    # Constructing a tree:
    #                   10
    #             33          22
    #          24    25    34    12
    #         1  2  3  4  5  6  7  8

    root = Node(10)

    root.left = Node(33)
    root.left.left = Node(24)
    root.left.left.left = Node(1)
    root.left.left.right = Node(2)
    root.left.right = Node(25)
    root.left.right.left = Node(3)
    root.left.right.right = Node(4)

    root.right = Node(22)
    root.right.left = Node(34)
    root.right.left.left = Node(5)
    root.right.left.right = Node(6)
    root.right.right = Node(12)
    root.right.right.left = Node(7)
    root.right.right.right = Node(8)


    print(sum_of_left_leaf_nodes(root))