import sys
from collections import deque
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

matirx = [list(input().strip()) for _ in range(12)]

def bfs(y,x):
    q = deque([(y,x)])
    temp = [(y,x)]

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < 12 and 0<= nx < 6 and not check[ny][nx]:
                if matirx[ny][nx] == matirx[y][x]:
                    check[ny][nx] = True
                    q.append((ny,nx))
                    temp.append((ny,nx))
    
    return temp

def delete(temp):
    for y, x in temp:
        matirx[y][x] = '.'

def down():
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if matirx[j][i] != '.' and matirx[k][i] == '.':
                    matirx[k][i] = matirx[j][i]
                    matirx[j][i] = '.'
                    break

count = 0
while True:
    puyo = False
    check = [[False]*6 for _ in range(12)]

    for j in range(12):
        for i in range(6):
            if matirx[j][i] != '.' and not check[j][i]:
                check[j][i] = True
                temp = bfs(j,i)

                if len(temp) >= 4:
                    puyo = True
                    delete(temp)
    
    if puyo == False:
        break
    down()
    count += 1

print(count)
