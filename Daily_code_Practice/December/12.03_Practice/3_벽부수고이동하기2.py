import sys
from collections import deque
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

n, m, k = map(int, input().split())
matrix = [list(map(int, input().strip()))for _ in range(n)]
check = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
check[0][0][k] = 1
pprint(check)



def bfs(y, x, z):
    q = deque([(y, x, z)])
    

    while  q:
        y, x, z = q.popleft()

        if (y, x) == (n-1, m-1):
            return check[y][x][z]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0<= nx < m:
                if check[ny][nx][z]:
                    continue
                if matrix[ny][nx] == 1 and z > 0:
                    check[ny][nx][z-1] = check[y][x][z] + 1
                    q.append((ny,nx,z-1))
                elif matrix[ny][nx] == 0 and check[ny][nx][z] == 0:
                    check[ny][nx][z] = check[y][x][z] + 1
                    q.append((ny,nx,z))
    return -1


print(bfs(0, 0, k))
pprint(matrix)
pprint(check)
