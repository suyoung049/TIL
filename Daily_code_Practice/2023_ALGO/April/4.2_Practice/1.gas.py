import sys
from collections import deque
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

dy = [0, 1, 0, -1, 1, 1, -1, -1] 
dx = [1, 0, -1, 0, 1, -1, 1, -1]

def bfs(y,x):
    check[y][x] = True
    q = deque([(y,x)])

    while q:
        y, x = q.popleft()

        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny <n and 0<= nx <m and not check[ny][nx]:
                if matrix[ny][nx] == '@':
                    check[ny][nx] = True
                    q.append((ny, nx))
while True:
    n, m = map(int, input().split())

    if n == 0:
        break
    
    else:
        matrix = [list(input().strip()) for _ in range(n)]
        check = [[False]*m for _ in range(n)]
        
        count_ = 0
        for j in range(n):
            for i in range(m):
                if matrix[j][i] == '@' and not check[j][i]:
                    bfs(j,i)
                    count_ += 1
    
    print(count_)


