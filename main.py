#!/usr/bin/env python3
from checkmate import checkmate
def main():
    board = """\
X . . X . . X
. X . X . X .
. . X X X . .
X X X Q X X X
. . X X X . .
. X . X . X .
X . . X . . X
\
"""
    checkmate(board)
if __name__  == "__main__":
    main()