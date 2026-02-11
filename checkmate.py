#!/usr/bin/env python3
def checkmate(board):
    if not board:
        print("ไม่พบบอร์ด")
        return
    board = board.strip()
    rows = board.split('\n')
    rows = [row.replace(" ", "") for row in rows]
    size = len(rows)
    for row in rows:
        if len(row) != size:
            print("ขนาดไม่ถูกต้อง")
            return
    count_k = 0
    for row in rows:
        count_k += row.count('K')
    if count_k!=1:
        print("Error_King")
        return
    king_x = -1
    king_y = -1
    for y_k,row in enumerate(rows):
        if 'K' in row:
            king_y = y_k
            king_x = row.index('K')
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),   
        (-1, -1), (-1, 1), (1, -1), (1, 1) 
    ]

    for dy, dx in directions:
        cur_y, cur_x = king_y + dy, king_x + dx
        
        while 0 <= cur_y < size and 0 <= cur_x < size:
            piece = rows[cur_y][cur_x]
            
            if piece != '.':
                
                is_straight = (dy == 0 or dx == 0)
                is_diagonal = (dy != 0 and dx != 0)

                if piece == 'Q':
                    print("Success")
                    return
                
                elif piece == 'R' and is_straight:
                    print("Success")
                    return
                
                elif piece == 'B' and is_diagonal:
                    print("Success")
                    return
                
                break 
            
            cur_y += dy
            cur_x += dx


    pawn_potential_positions = [
        (king_y + 1, king_x - 1), 
        (king_y + 1, king_x + 1)
    ]
    
    for py, px in pawn_potential_positions:
        if 0 <= py < size and 0 <= px < size:
            if rows[py][px] == 'P':
                print("Success")
                return

    print("Fail")