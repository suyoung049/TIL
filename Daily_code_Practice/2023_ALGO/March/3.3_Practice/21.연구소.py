import sys
from itertools import combinations
from collections import deque
sys.stdin = open('21_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def pprint(list_):
    for row in list_:
        print(row)

matrix = [list(input().split()) for _ in range(n)]
pprint(matrix)
INF = sys.maxsize


def bfs(q, blanck_count):
    check = [[-1]*n for _ in range(n)]

    time = 0

    while True:

        if blanck_count == 0 or len(q) == 0:  # while q
            if blanck_count == 0:
                return time
            else:
                return INF
    
        time += 1

        for i in range(len(q)):  # 1초에 전염되는 바이러스의 수 

            y, x = q.popleft()

            if check[y][x] == -1:
                check[y][x] = 1
            
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0<= ny < n and 0<= nx < n:
                    if check[ny][nx] == -1:
                        if matrix[ny][nx] == 0:
                            check[ny][nx] = True
                            q.append((ny,nx))
                            blanck_count -= 1
                        elif matrix[ny][nx] == 2:
                            q.append((ny,nx))
                            check[ny][nx] = True

virous = []
blanck_count = 0

for j in range(n):
    for i in range(n):
        if matrix[j][i] == 2:
            virous.append((j,i))
        elif matrix[j][i] == 0:
            blanck_count += 1

res = INF
for vir_li in combinations(virous, m):
    q = deque()
    for vir in vir_li:
        q.append(vir)
    temp = bfs(q, blanck_count)
    res = min(res, temp)

if res == INF:
    print(-1)

else:
    print(res)