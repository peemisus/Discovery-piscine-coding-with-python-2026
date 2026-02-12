#!/usr/bin/env python3
from checkmate import checkmate
def main():
    board = """\
.......
.......
.Q.P...
..B....
...R...
.......
....K..
\
"""
    checkmate(board)
if __name__  == "__main__":
    main()
    
"""
Test case for checkmate.py
.....
.K..Q
...P.
..B..
...R.
Success

.....
.K...
...P.
..B..
...R.
Fail

.....
.K...
...P.
..B..
...R..Q
ขนาดไม่ถูกต้อง

.....
.K...
...P.
..B..
...K.
Error_King

.....
.....
...P.
..B..
...R.
Error_King
"""