import sys
sys.stdin = open('8_input.txt', 'r')
from collections import deque
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

n, m = map(int, input().split())

matrix = list(list(map(int, input().strip())) for _ in range(n))
check = [[[0]*2 for _ in range(m)] for _ in range(n)]
check[0][0][0] = 1





def bfs(x, y, z):
    q = deque([(x,y,z)])

    while q:
        y, x, z = q.popleft()

        if (y, x) ==  (n-1, m-1):
            return check[y][x][z]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0<= nx <m:
                if matrix[ny][nx] == 0 and check[ny][nx][z] == 0:
                    check[ny][nx][z] =  check[y][x][z] + 1
                    q.append((ny,nx,z))
                if matrix[ny][nx] == 1 and z == 0:
                    check[ny][nx][1] = check[y][x][0] + 1
                    q.append((ny,nx,1))
    return -1


bfs(0,0,0)
pprint(check)

