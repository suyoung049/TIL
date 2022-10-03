import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
sys.stdin = open('6_input.txt', 'r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]
check = [[False] *n for _ in range(n)]
inf = sys.maxsize

def bfs(c):
    global inf
    check = [[-1] * n for _ in range(n)]
    q = deque()

    for j in range(n):
        for i in range(n):
            if matrix[j][i] == c:
                check[j][i] = 0
                q.append((j,i))
    
    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0<= nx < n:
                
                if matrix[ny][nx] == 0 and check[ny][nx] == -1:
                    check[ny][nx] = check[y][x] + 1
                    q.append((ny,nx))

                if matrix[ny][nx] > 0 and matrix[ny][nx] != c:
                    inf = min(inf, check[y][x])
                    return



def dfs(y, x, c):
    matrix[y][x] = c

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0<= ny < n and 0<= nx < n and not check[ny][nx]:
            if matrix[ny][nx] == 1:
                matrix[ny][nx] = c
                check[ny][nx] = True
                dfs(ny, nx, c)


count = 0
for j in range(n):
    for i in range(n):
        if matrix[j][i] == 1 and not check[j][i]:
            check[j][i] = True
            count += 1
            dfs(j, i, count)

for i in range(1, count+1):
    bfs(i)

print(inf)

