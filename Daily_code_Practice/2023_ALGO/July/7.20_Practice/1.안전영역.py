import sys
from collections import deque
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

def bfs(y, x):
    
    q = deque([(y,x)])
    check[y][x] = True

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0<= nx < n and not check[ny][nx]:
                if water_check[ny][nx] == 0 :
                    check[ny][nx] = True
                    q.append((ny, nx))

water_high = 0

for j in range(n):
    for i in range(n):
        if matrix[j][i] > water_high:
            water_high = matrix[j][i]

result = 0
for safe_high in range(water_high):
    water_check = [[0] * n for _ in range(n)]
    safe_area = 0
    for j in range(n):
        for i in range(n):
            if matrix[j][i] <= safe_high:
                water_check[j][i] = 1
    
    check = [[False] * n for _ in range(n)]
    for j in range(n):
        for i in range(n):
            if water_check[j][i] == 0 and not check[j][i]:
                safe_area += 1
                bfs(j,i)
            
    
    result = max(result, safe_area)
        

    
print(result)