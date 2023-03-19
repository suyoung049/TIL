import sys
from collections import deque
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

matrix = [list(map(int, input().strip())) for _ in range(n)]
check = [[False]* m for _ in range(n)]

def bfs(y, x, rode):
    check[y][x] = True

    q = deque([(y, x, rode)])

    while q:
        y, x, rode  = q.popleft()

        if (y, x) == (n-1, m-1):
            return rode

        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0<= nx < m and not check[ny][nx]:
                if matrix[ny][nx] == 1:
                    check[ny][nx] = True
                    q.append((ny, nx, rode+1))

print(bfs(0, 0, 1))