import sys
from collections import deque
sys.stdin = open('5_input.txt', 'r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)


N, M, K = map(int, input().split())
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

map = [[0]*M for _ in range(N)]
check = [[False]*M for _ in range(N)]

for _ in range(K):
    
    x1, y1, x2, y2 = input().split()
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)

    for j in range(y1,y2):
        for i in range(x1,x2):
            map[j][i] = 1
pprint(map)

def bfs(y,x):
    size = 1
    check[y][x] = True
    q = deque([(y,x)])

    while q:
        ey, ex = q.popleft()

        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]

            if 0<=ny<N and 0<=nx<M:
                if map[ny][nx] == 0 and check[ny][nx] == False:
                    check[ny][nx] = True
                    size += 1
                    q.append((ny,nx))
    return size



result = []
coun = 0
for k in range(N):
    for m in range(M):

        if map[k][m] == 0 and check[k][m] == False:
            check[k][m] = True
            coun += 1
            result.append(bfs(k,m))
sr_result = sorted(result)
print(coun)
for i in sr_result:
    print(i, end = ' ')

    





