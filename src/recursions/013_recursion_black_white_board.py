# !/usr/bin/env python3
# encoding: utf-8

"""
    Find if a given black is conquered in the board game Go.
        black and white play alternately.
        black is conquered if it is (and all its neighboring blacks, if any, are also) surrounded by whites or borders of the board.
        board size is 19x19

    @author: Mohammed Ataaur Rahaman
"""

BLACK = 'Black'
WHITE = 'White'
EMPTY = None

BOARD = [
    [EMPTY, WHITE, BLACK],
    [EMPTY, WHITE, BLACK],
    [EMPTY, EMPTY, EMPTY],
]
ROW = len(BOARD)
COL = len(BOARD[0])


def is_captured(i, j, visited):
    if visited[i][j]:
        return True

    if BOARD[i][j] == EMPTY:
        return False

    if BOARD[i][j] == WHITE:
        return True

    visited[i][j] = True
    # Move left
    if j > 0 and not is_captured(i, j - 1, visited):
        return False

    # Move Right
    if j < COL - 1 and not is_captured(i, j + 1, visited):
        return False

    # Move Up
    if i > 0 and not is_captured(i - 1, j, visited):
        return False

    # Move Down
    if i < ROW - 1 and not is_captured(i + 1, j, visited):
        return False

    return True


def is_captured1(i, j, visited):
    if BOARD[i][j] == EMPTY:
        return False

    if BOARD[i][j] == WHITE or visited[i][j]:
        return True

    visited[i][j] = True
    if (j > 0 and not is_captured1(i, j - 1, visited)) or \
            (j < COL - 1 and not is_captured1(i, j + 1, visited)) or \
            (i > 0 and not is_captured1(i - 1, j, visited)) or \
            (i < ROW - 1 and not is_captured1(i + 1, j, visited)):
        return False

    return True


if __name__ == '__main__':
    visited = [[False]*COL for i in range(ROW)]
    print(is_captured(0, 2, visited=visited))

    visited = [[False] * COL for i in range(ROW)]
    print(is_captured1(0, 2, visited=visited))
