import sys
from collections import deque
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

n, m, k = map(int, input().split())

matrix = [['.']*m for _ in range(n)]
check = [[False]*m for _ in range(n)]

for _ in range(k):
    y, x = map(int, input().split())
    matrix[y-1][x-1] = '#'

def bfs(y,x):
    result = 1

    q = deque([(y,x)])

    while q:

        (y,x) = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and not check[ny][nx]:
                if matrix[ny][nx] == '#':
                    check[ny][nx] = True
                    q.append((ny,nx))
                    result += 1
    return result

answer = 0

for j in range(n):
    for i in range(m):
        if matrix[j][i] == '#' and not check[j][i]:
            check[j][i] = True
            answer = max(answer, bfs(j,i))

print(answer)