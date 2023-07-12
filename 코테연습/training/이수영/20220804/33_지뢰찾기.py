import sys

sys.stdin = open("33_input.txt", "r")
def pprint(list_):
    for row in list_:
        print(row)

dy = [-1, -1, -1, 0, 0, 1, 1, 1 ]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

boom = '*'
empty = '.'

n = int(input())

game_bord = [list(input()) for _ in range(n)]
open_bord = [list(input()) for _ in range(n)]
result = []
for i in range(n):
    list_ = ['.'] * n
    result.append(list_)

game_bord = list(game_bord)
open_bord = list(open_bord)
find_boom = False
for y in range(n):
    for x in range(n):
        if open_bord[y][x] == 'x':
            boom_coun = 0
            for d in range(8):
                find_y = y + dy[d]
                find_x = x + dx[d] 

                if 0<= find_y <= n-1 and 0<= find_x <= n-1:

                    if game_bord[find_y][find_x] == boom:
                        boom_coun += 1
            result[y][x] = str(boom_coun)

            if game_bord[y][x] == boom:
                find_boom = True

if find_boom == True:

    for y in range(n):
        for x in range(n):
            if game_bord[y][x] == boom:
                result[y][x] = boom

for row in result:
    print(''.join(row))
     
