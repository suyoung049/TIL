import sys
from collections import deque
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(n)]

chek = [[False] * m for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x):
    rs = 1
    q = deque([(y, x)])
    chek[y][x] = True
    
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]

            if 0<= ny <n and 0<=nx<m :
                if map[ny][nx] == 1 and chek[ny][nx] == False:
                    chek[ny][nx] = True
                    rs += 1
                    q.append((ny,nx))
    
    return rs

coun = 0
max_ = 0
for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chek[j][i] == False:
            chek[j][i] = True
            coun += 1
            max_ = max(max_, bfs(j,i)) 

print(coun)
print(max_)
