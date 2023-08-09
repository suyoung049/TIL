import sys
sys.stdin = open("1_input.txt", "r")


row_li = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7}
revers = {0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H"}

move_li = ["R","L","B","T","RT","LT","RB","LB"]

dy = [0, 0, 1, -1, -1, -1, 1, 1]
dx = [1, -1, 0, 0, 1, -1, 1, -1]

king, stone, move_cnt = input().split()

move_cnt = int(move_cnt)

king_y = 8 - int(king[1])
king_x = row_li[king[0]]

stone_y = 8 - int(stone[1])
stone_x = row_li[stone[0]]

for _ in range(move_cnt):
    move = input()
    idx = move_li.index(move)

    king_ny = king_y + dy[idx]
    king_nx = king_x + dx[idx]

    if 0<= king_ny < 8 and 0<= king_nx < 8:
        if king_ny == stone_y and king_nx == stone_x:
            stone_ny = stone_y + dy[idx]
            stone_nx = stone_x + dx[idx]

            if 0<= stone_ny < 8 and 0<= stone_nx< 8:
                stone_y, stone_x = stone_ny, stone_nx
                king_y, king_x = king_ny, king_nx
            else:
                continue
        else:
            king_y, king_x = king_ny, king_nx
    else:
        continue


print(revers[king_x] + str(8-king_y))
print(revers[stone_x] + str(8-stone_y))