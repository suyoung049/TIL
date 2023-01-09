import sys
from collections import deque
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

n, m = map(int, input().split())

matrix = list(list(input().strip()) for _ in range(n))

def bfs(j,i):
    check = [[0]*m for _ in range(n)]
    check[j][i] = 1
    q = deque([(j,i)])
    result = 0

    while q:

        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0<= nx < m:
                if check[ny][nx] == 0 and matrix[ny][nx] == 'L':
                    check[ny][nx] = check[y][x] + 1
                    q.append((ny,nx))
                    result = max(result, check[ny][nx])


    return result - 1


result = 0
for j in range(n):
    for i in range(m):
        if matrix[j][i] == 'L':
            result = max(result, bfs(j,i))

print(result)