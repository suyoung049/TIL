import sys
from collections import deque
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

def pprint(list_):
    for row in list_:
        print(row)

n, m, k = map(int, input().split())

matrix = [['.']*m for _ in range(n)]
check = [[False]*m for _ in range(n)]



for _ in range(k):
    r, c = map(int, input().split())
    matrix[r-1][c-1] = 'X'

def bfs(y, x):
    size = 1
    q = deque([(y,x)])

    while q:

        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0<= nx < m and check[ny][nx] == False:
                if matrix[ny][nx] == 'X':
                    check[ny][nx] = True
                    size += 1
                    q.append((ny,nx))
    return size


result = []
for j in range(n):
    for i in range(m):
        if matrix[j][i] == 'X' and check[j][i] == False:
            check[j][i] = True
            result.append(bfs(j,i))

print(result)

