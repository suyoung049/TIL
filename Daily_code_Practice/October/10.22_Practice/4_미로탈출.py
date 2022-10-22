import sys
from collections import deque
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def pprint(list_):
    for row in list_:
        print(row)

n, m = map(int, input().split())
sy, sx = map(int, input().split())
fy, fx = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
check = [[[0]*2 for _ in range(m)] for _ in range(n)]

check[sy-1][sx-1][0] = 1

def bfs(y, x, z):
    q = deque([(y,x,z)])

    while q:
        y, x, z = q.popleft()

        if (y, x) == (fy-1, fx-1):
            return check[y][x][z] - 1

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0<= nx < m:
                if matrix[ny][nx] == 1 and z == 0:
                    check[ny][nx][1] = check[y][x][0] + 1
                    q.append((ny,nx,1))

                elif matrix[ny][nx] == 0 and check[ny][nx][z] == 0:
                    check[ny][nx][z] = check[y][x][z] + 1
                    q.append((ny,nx,z))

    return -1

print(bfs(sy-1,sx-1,0))



    



