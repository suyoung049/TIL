import sys
from collections import deque
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

n, k = map(int, input().split())

martix = [list(map(int, input().split())) for _ in range(n)]
check = [[False] * n for _ in range(n)]

time, r_y, r_x = map(int, input().split())




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

                if 0<= ny < n and 0<= nx < n and not check[ny][nx]:
                    if martix[ny][nx] == 0:
                        martix[ny][nx] = kind
                        check[ny][nx] = True
                        q.append((kind, ny, nx))
        count_ += 1
        
        
virous = []
for j in range(n):
    for i in range(n):
        if martix[j][i] != 0:
            check[j][i] = True
            virous.append((martix[j][i], j, i))

virous.sort()

bfs(virous)


print(martix[r_y-1][r_x-1])
