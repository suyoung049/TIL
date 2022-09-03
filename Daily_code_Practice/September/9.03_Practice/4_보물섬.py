import sys
from collections import deque
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

N, M = map(int, input().split())

map = [list(input().strip()) for _ in range(N)]


def bfs(y,x):
    count = 0
    q = deque([(y,x)])
    check = [[0]*M for _ in range(N)]
    check[y][x] = 1
    
    while q:
        ey, ex = q.popleft()

        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]

            if 0<= ny < N and 0<= nx < M:
                if map[ny][nx] == 'L' and check[ny][nx] == 0:
                    check[ny][nx] = (check[ey][ex] + 1)
                    count = max(count, check[ny][nx])
                    q.append((ny,nx))
    return count-1


result = 0
for j in range(N):
    for i in range(M):
        if map[j][i] == 'L':
            result = max(result,bfs(j,i))

print(result)

