import sys
sys.stdin = open("1_input.txt", "r")
from collections import deque
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
check = [[0] * m for _ in range(n)]

def bfs(virous):
    q = deque(virous)
    one_check = []    

    while q:
        if one_check:
 
            for _ in range(len(one_check)):
                one_y, one_x = one_check.pop()
                if matrix[one_y][one_x] == 1 and not check[one_y][one_x]:
                    check[one_y][one_x] = 1
        
        for _ in range(len(q)):

            kind, y, x = q.popleft()

            if matrix[y][x] == 3:
                continue

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0<= ny < n and 0<= nx <m and not check[ny][nx]:
                    if kind == 1:
                        if matrix[ny][nx] == 0:
                            matrix[ny][nx] = 1
                            one_check.append((ny, nx))
                            q.append((kind, ny, nx))
                    elif kind == 2:
                        if matrix[ny][nx] == 0:
                            matrix[ny][nx] = 2
                            check[ny][nx] = 1
                            q.append((kind, ny, nx))
                        elif matrix[ny][nx] == 1:
                            matrix[ny][nx] = 3
                            check[ny][nx] = 1
                                    
virous = []
for j in range(n):
    for i in range(m):
        if matrix[j][i] == 1:
            check[j][i] = 1
            virous.append((1, j, i))
        elif matrix[j][i] == 2:
            check[j][i] = 1
            virous.append((2, j, i))

virous.sort()
bfs(virous)

answer = [0, 0, 0]

for j in range(n):
    for i in range(m):
        if matrix[j][i] == 1:
            answer[0] += 1
        elif matrix[j][i] == 2:
            answer[1] += 1
        elif matrix[j][i] == 3:
            answer[2] += 1

print(*answer)

