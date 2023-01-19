import sys
from collections import deque
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def pprint(list_):
    for row in list_:
        print(row)

n, m  = map(int, input().split())

matrix = list(list(input().strip()) for _ in range(n))

check = [[False]*m for _ in range(n)]

result = 0

def w_bfs(y,x):
    q = deque([(y,x)])

    while q:
        (y,x) = q.popleft()

        for i in range(2):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0<= nx <m and not check[ny][nx]:
                if matrix[ny][nx] == '-':
                    check[ny][nx] = True
                    q.append((ny,nx))


def l_bfs(y,x):
    q = deque([(y,x)])

    while q:
        (y,x) = q.popleft()

        for i in range(2, 4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0<= nx <m and not check[ny][nx]:
                if matrix[ny][nx] == '|':
                    check[ny][nx] = True
                    q.append((ny,nx))


for j in range(n):
    for i in range(m):
        if matrix[j][i] == '-' and not check[j][i]:
            check[j][i] = True
            w_bfs(j,i)
            result += 1



for j in range(n):
    for i in range(m):
        if matrix[j][i] == '|' and not check[j][i]:
            check[j][i] = True
            l_bfs(j,i)
            result += 1

print(result)