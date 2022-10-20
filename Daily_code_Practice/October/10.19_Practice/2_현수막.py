import sys
sys.stdin = open('2_input.txt', 'r')
from collections import deque
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

dy = [0, 1, 0, -1, 1, 1, -1, -1]
dx = [1, 0, -1, 0, 1, -1, -1, 1]

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
check = [[False]*m for _ in range(n)]


def bfs(y, x):
    q = deque([(y,x)])

    check[y][x] = True

    while q:
        y, x = q.popleft()

        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0<= nx < m and not check[ny][nx]:
                if matrix[ny][nx] == 1:
                    check[ny][nx] = True
                    q.append((ny,nx))

text = 0    
for j in range(n):
    for i in range(m):
        if matrix[j][i] == 1 and not check[j][i]:
            text += 1
            bfs(j,i)

print(text)



