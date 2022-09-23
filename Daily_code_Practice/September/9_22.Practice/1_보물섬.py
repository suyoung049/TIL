import sys
from collections import deque
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

def pprint(list_):
    for row in list_:
        print(row)

n, m = map(int, input().split())

matrix = [list(input().strip()) for _ in range(n)]


def bfs(y, x):
    visit = [[0] * m for _ in range(n)]
    max_ = 0
    q = deque([(y,x)])
    

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny <n and 0<=nx <m and visit[ny][nx] == 0:
                if matrix[ny][nx] == 'L':
                    visit[ny][nx] = visit[y][x] + 1
                    max_ = max(max_, visit[ny][nx])
                    q.append((ny, nx))
    return max_

result = 0
for j in range(n):
    for i in range(m):
        if matrix[j][i] == 'L':
            result = max(result, bfs(j,i))

print(result)



