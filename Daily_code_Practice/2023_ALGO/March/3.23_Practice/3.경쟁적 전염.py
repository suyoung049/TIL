import sys
from collections import deque
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

n, k = map(int, input().split())

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

matrix = [list(map(int, input().split())) for _ in range(n)]
virous_check = [[False] * n for _ in range(n)]


time, end_y, end_x = map(int, input().split())


def bfs(virous):
    q = deque(virous)
    count_ = 0

    while q:
        if count_ == time:
            break
        
        for _ in range(len(q)):
            kind, y, x = q.popleft()

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0<= ny < n and 0<= nx < n and not virous_check[ny][nx]:
                    if matrix[ny][nx] == 0:
                        matrix[ny][nx] = kind
                        virous_check[ny][nx] = True
                        q.append((kind, ny, nx))
        
        count_ += 1

virous = []

for j in range(n):
    for i in range(n):
        if matrix[j][i] != 0:
            virous_check[j][i] = True
            virous.append((matrix[j][i], j, i))

virous.sort()

bfs(virous)

print(matrix[end_y-1][end_x-1])