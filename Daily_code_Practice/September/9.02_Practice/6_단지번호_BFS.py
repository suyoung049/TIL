import sys
sys.stdin = open('1_input.txt', 'r')
from collections import deque
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

n = int(input())

map = [list(map(int, input().strip())) for _ in range(n)]

check = [[False]*n for _ in range(n)]

def bfs(y, x):
    size = 1
    stack = deque([(y,x)])
    check[y][x] = True
    
    while stack:
        ey, ex = stack.popleft()

        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]

            if 0<=ny<n and 0<=nx<n:
                if map[ny][nx] == 1 and check[ny][nx] == False:
                    check[ny][nx] = True
                    size += 1
                    stack.append((ny,nx))
        
    return size



count = 0
result = []
for j in range(n):
    for i in range(n):
        if map[j][i] == 1 and check[j][i] == False:
            check[j][i] == True
            count += 1
            result.append(bfs(j,i))

sr_result = sorted(result)
print(count)
print(sr_result)

