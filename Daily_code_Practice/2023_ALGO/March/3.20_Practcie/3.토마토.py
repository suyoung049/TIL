import sys
from collections import deque
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline


dz = [0, 0, 0, 0, 1, -1]
dy = [1, 0, -1, 0, 0, 0]
dx = [0, 1, 0, -1, 0, 0]


m, n, h = map(int, input().split())

matrix = [[list(map(int, input().split())) for _ in range(n)]  for _ in range(h)]
check = [[[False]*m for _ in range(n)] for _ in range(h)]


def bfs(q, check):
    global empty
    
    day = 0

    while True:
        tomato_n = len(q)

        if empty == 0 or tomato_n == 0:
            
            if empty == 0:
                break
            else:
                day = -1
                break


        for _ in range(tomato_n):
            z, y, x = q.popleft()

            for i in range(6):
                nz = z + dz[i]
                ny = y + dy[i]
                nx = x + dx[i] 

                if 0 <= nz < h and 0 <= ny < n and 0 <= nx <m:
                    if matrix[nz][ny][nx] == 0 and not check[nz][ny][nx]:
                        check[nz][ny][nx] = True
                        empty -= 1
                        q.append((nz,ny,nx))
        
        day += 1
    return day

empty = 0
q = deque()
for k in range(h):
    for j in range(n):
        for i in range(m):
            if matrix[k][j][i] == 0:
                empty += 1
            elif matrix[k][j][i] == 1 and not check[k][j][i]:
                q.append((k, j, i))
                check[k][j][i] = True


if empty == 0:
    print(0)

else:
    print(bfs(q, check))


