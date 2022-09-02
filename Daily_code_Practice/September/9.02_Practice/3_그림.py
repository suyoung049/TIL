import sys
from collections import deque
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(N)]

check = [[False]*M for _ in range(N)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y,x):
    size = 1
    q = deque([(y,x)])
    check[y][x] == True
    while q:
        ey, ex = q.popleft()

        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]

            if 0<=ny <N and 0<=nx <M:
                if map[ny][nx] == 1 and check[ny][nx] == False:
                    check[ny][nx] = True
                    size += 1
                    q.append((ny,nx))
    
    return size



coun = 0
max_ = 0
for j in range(N):
    for i in range(M):
        if map[j][i] == 1 and check[j][i] == False:
            check[j][i] = True
            coun += 1
            max_ = max(max_, bfs(j,i))
            

print(coun)
print(max_)
