import sys
sys.stdin = open('5_input.txt', 'r')
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

matrix = [list(input().strip()) for _ in range(n)]
walk_check = [[0]*m for _ in range(n)]
water_check = [[False]*m for _ in range(n)]

def bfs(end_y, end_x, q):

    while q:
        y, x, type_ = q.popleft()

        if (y, x, type_) == (end_y, end_x, 'S'):
            return walk_check[y][x]
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
        
            if 0<= ny < n and 0<= nx< m:
                if (matrix[ny][nx] == '.' or matrix[ny][nx] == 'D') and matrix[y][x] != '*':
                    if not walk_check[ny][nx] and type_ == 'S':
                        walk_check[ny][nx] = walk_check[y][x] + 1
                        q.append((ny, nx, 'S'))
                    
                elif matrix[ny][nx] == '.' and not water_check[ny][nx] and type_ == '*':
                        water_check[ny][nx] = True
                        matrix[ny][nx] = '*'
                        q.append((ny,nx, '*'))
            
    return 'KAKTUS'
  
q = deque()

for j in range(n):
    for i in range(m):
        if matrix[j][i] == "S":
            q.append((j, i, 'S'))
        
        elif matrix[j][i] =='D':
            end_y, end_x = j, i

for j in range(n):
    for i in range(m):
        if matrix[j][i] == '*':
            q.append((j, i, '*'))


print(bfs(end_y, end_x, q))