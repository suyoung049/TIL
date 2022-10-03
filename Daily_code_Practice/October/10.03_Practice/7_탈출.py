import sys
from collections import deque
sys.stdin = open('7_input.txt', 'r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

n, m = map(int, input().split())

matrix = [list(input().strip()) for _ in range(n)]
check = [[0] * m for _ in range(n)]
q = deque()


def bfs(ky, kx):

    while q:

        y, x = q.popleft()

        if matrix[ky][kx] == 'S':
            return check[ky][kx]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0<= nx < m:
                if (matrix[ny][nx] == '.' or matrix[ny][nx] == 'D') and matrix[y][x] == 'S':
                    matrix[ny][nx] = 'S'
                    check[ny][nx] = check[y][x] + 1
                    q.append((ny,nx))
                
                elif (matrix[ny][nx] == '.' or matrix[ny][nx] == 'S') and matrix[y][x] == '*':
                    matrix[ny][nx] = '*'
                    q.append((ny,nx))
                


for j in range(n):
    for i in range(m):
        if matrix[j][i] == 'S':
            q.append((j,i))

        elif matrix[j][i] == 'D':
            ky, kx = j, i

for j in range(n):
    for i in range(m):
        if matrix[j][i] == '*':
            q.append((j,i))

result = bfs(ky,kx)

if not result:
    print('KAKTUS')
else:
    print(result)