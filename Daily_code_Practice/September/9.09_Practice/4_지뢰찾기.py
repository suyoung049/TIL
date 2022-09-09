import sys
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)
dy = [-1, -1, -1, 0, 0, 1, 1, 1 ]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

n = int(input())
game_bord = [list(input().strip()) for _ in range(n)]
user_bord = [list(input().strip()) for _ in range(n)]
result_bord = [['.']*n for _ in range(n)]
check = False

for y in range(n):
    for x in range(n):
        if user_bord[y][x] == 'x':
            count = 0 
            
            if game_bord[y][x] == '*':
                check = True

            for i in range(8):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0<= ny < n and 0<= nx < n :
                    if game_bord[ny][nx] == '*':
                        count += 1
            result_bord[y][x] = str(count)
        

if check == True:
    for y in range(n):
        for x in range(n):
            if game_bord[y][x] == "*":
                result_bord[y][x] = '*'

for i in result_bord:
    print(''.join(i))


