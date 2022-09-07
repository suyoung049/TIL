import sys
from collections import deque
sys.stdin = open('5_input.txt', 'r')
input = sys.stdin.readline
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

n, m = map(int, input().split())

map = [list(map(int, input().strip())) for _ in range(n)]

visit = [[0] *m for _ in range(n)]

def bfs():
    
    q = deque([(0,0)])
    visit[0][0] = 1

    while q:
        (y,x) = q.popleft()

        if (y,x) == (n-1,m-1):
            return (visit[y][x])

        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0<= nx < m:
                if map[ny][nx] == 1 and visit[ny][nx] == 0:
                    visit[ny][nx] = visit[y][x] + 1
                    q.append((ny,nx))

print(bfs())



