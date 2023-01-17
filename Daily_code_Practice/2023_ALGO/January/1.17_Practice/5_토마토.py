import sys
from collections import deque
sys.stdin = open('5_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())

def pprint(list_):
    for row in list_:
        print(row)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

matrix = list(list(map(int, input().split())) for _ in range(m))
check = [[0] * n for _ in range(m)]

def bfs():


    while q:
        (y, x) = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < m and 0<= nx < n and matrix[ny][nx] == 0:
                if check[ny][nx] == 0:
                    check[ny][nx] = check[y][x] + 1
                    q.append((ny,nx))
q = []
for j in range(m):
    for i in range(n):
        if matrix[j][i] == 1:
            check[j][i] = 1
            q.append((j,i))
q = deque(q)
bfs()
           

pprint(check)
answer = 0
ch = False

for j in range(m):
    for i in range(n):
        if check[j][i] == 0 and matrix[j][i] == 0:
            ch = True
            break
        else:
            answer = max(answer,  check[j][i]-1)

if ch:
    print(-1)

else:
    print(answer)

