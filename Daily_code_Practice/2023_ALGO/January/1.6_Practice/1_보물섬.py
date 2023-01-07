import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline
from collections import deque

def pprint(list_):
    for row in list_:
        print(row)

dy = [0, 1, -1, 0]
dx = [1, 0, 0, -1]

n, m = map(int, input().split())

matrix = list(list(input().strip()) for _ in range(n))

def bfs(y, x):
    count = 0
    check = [[0]*m for _ in range(n)]
    check[y][x] = 1
    q = deque([(y,x)])

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0<= nx < m and not check[ny][nx]:
                if matrix[ny][nx] == 'L':
                    check[ny][nx] = check[y][x] + 1
                    count = max(count, check[ny][nx])
                    q.append((ny,nx))
    
    return count - 1


result = 0
for j in range(n):
    for i in range(m):
        if matrix[j][i] == 'L':
            result = max(result, bfs(j, i))

print(result)
