import sys
sys.stdin = open('1_input.txt', 'r')
from collections import deque
input = sys.stdin.readline

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def pprint(list_):
    for row in list_:
        print(row)

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]

count = 0

def bfs(y,x):
    q = deque([(y,x)])

    while q:
        (y, x) = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0<= nx <m and not check[ny][nx]:
                if temp[ny][nx] != 0:
                    check[ny][nx] = True
                    q.append((ny,nx))

while True:
    temp = [[0] *m for _ in range(n)]
    for j in range(n):
        for i in range(m):
            
            if map[j][i] != 0:
                stack = 0
                
                for k in range(4):
                    ny = j + dy[k]
                    nx = i + dx[k]

                    if map[ny][nx] == 0:
                        stack += 1
                
                temp[j][i] = map[j][i] - stack
                if temp[j][i] < 0:
                    temp[j][i] = 0
    count += 1

    ice = 0
    check = [[False]*m for _ in range(n)]

    for y in range(n):
        for x in range(m):
            if temp[y][x] != 0 and not check[y][x]:
                check[y][x] = True
                bfs(y,x)
                ice += 1
    zero = True   
    
    if ice > 1:
        break

    else:
        for j in range(n):
            for i in range(m):
                map[j][i] = temp[j][i]
                if map[j][i] != 0:
                    zero = False
        
        if zero == True:
            count = 0
            break

print(count)
