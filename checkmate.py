#!/usr/bin/env python3

"""
1. size board n x n (จัตุรัส)
2. ตัว K มีตัวเดียว
3. ตัวอักษรที่ใช้ได้: K, Q, R, B, P
4. เช็คว่า K ถูก check ไหม
5. ถ้า K ถูก check ให้ print "Success"
6. ถ้า K ไม่ถูก check ให้ print "Fail"
7. กรณีที่บอร์ดไม่ถูกต้อง ให้ print "ขนาดไม่ถูกต้อง"

ดัก error:
- ขนาดไม่ถูกต้อง
- Error_King (ไม่มี K หรือ มีมากกว่า 1 ตัว)
- ตัวอักษรไม่ถูกต้อง : !{., K, Q, R, B, P}
- ไม่พบบอร์ด
"""

def check_size_board(board):
    if not board:
        return None, "ไม่พบบอร์ด"
    board = board.strip()
    rows = board.split('\n')
    rows = [row.replace(" ", "") for row in rows]
    allowed = {'.', 'K', 'Q', 'R', 'B', 'P'}
    size = len(rows)
    for row in rows:
        if len(row) != size:
            return None, "ขนาดไม่ถูกต้อง"
        for ch in row:
            if ch not in allowed:
                return None, f"ตัวอักษรไม่ถูกต้อง : {ch}"
    return rows, None


def find_king(rows):
    count_k = sum(row.count('K') for row in rows)
    if count_k != 1:
        return None, "Error_King"
    for y_k, row in enumerate(rows):
        if 'K' in row:
            return (y_k, row.index('K')), None
    return None, "Error_King"

def in_bounds(y, x, size):
    return 0 <= y < size and 0 <= x < size


def check_by_slider(rows, king_y, king_x):
    size = len(rows)
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    ] # ตรวจเรียง ↑,↓,←,→,↖,↗,↙,↘

    for dy, dx in directions:
        cur_y, cur_x = king_y + dy, king_x + dx
        print(cur_y, cur_x, "->", dy, dx)
        while in_bounds(cur_y, cur_x, size):
            print(cur_y, cur_x)
            piece = rows[cur_y][cur_x]
            if piece != '.':
                is_straight = (dy == 0 or dx == 0)
                is_diagonal = (dy != 0 and dx != 0)

                if piece == 'Q': # 8 ทิศ
                    print("Found Q at", cur_y, cur_x, "direction", dy, dx)
                    return True
                if piece == 'R' and is_straight: # 4 ทิศ (10, 01, -10, 0-1)
                    return True
                if piece == 'B' and is_diagonal: # 4 ทิศ (11, 1-1, -11, -1-1)
                    return True
                break
            cur_y += dy
            cur_x += dx
    return False


def check_by_pawn(rows, king_y, king_x):
    size = len(rows)
    pawn_atk_king_pos = [
        (king_y + 1, king_x - 1),
        (king_y + 1, king_x + 1)
    ]
    for py, px in pawn_atk_king_pos:
        if in_bounds(py, px, size) and rows[py][px] == 'P':
            return True
    return False


def checkmate(board):
    try:
        rows, error = check_size_board(board)
        if error:
            print(error)
            return

        king_pos, error = find_king(rows)
        if error:
            print(error)
            return
        king_y, king_x = king_pos
        if check_by_slider(rows, king_y, king_x):
            print("Success") # Rook, Bishop, Queen
            return
        if check_by_pawn(rows, king_y, king_x):
            print("Success") # Only Pawn
            return

        print("Fail")
        
    except Exception as err:
        print("Error:", err)
        return