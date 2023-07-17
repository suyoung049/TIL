import sys
sys.stdin = open("2_input.txt", "r")
from collections import deque
input = sys.stdin.readline

k = int(input())

def pprint(list_):
    for row in list_:
        print(row)

monky_y = [0, 1, 0, -1]
monky_x = [1, 0, -1, 0]
horse_y = [1, 1, -1, -1, 2, 2, -2, -2]
horse_x = [2, -2, 2, -2, 1, -1, 1, -1]


m, n = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
check = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]



def bfs(z, y, x):
    q = deque([(y,x,z)])

    while q:
        y, x, z = q.popleft()

        if (y, x) == (n-1, m-1):
            return check[y][x][z]
        

        for i in range(4):
            ny = y + monky_y[i]
            nx = x + monky_x[i]

            if 0<= ny < n and 0<= nx < m and not check[ny][nx][z]:
                if matrix[ny][nx] != 1:
                    check[ny][nx][z] = check[y][x][z] + 1
                    q.append((ny, nx, z))
        

        if z < k:
            for i in range(8):
                ny = y + horse_y[i]
                nx = x + horse_x[i]

                if 0< ny < n and 0<= nx <m and not check[ny][nx][z+1]:
                    if matrix[ny][nx] != 1:
                        check[ny][nx][z+1] = check[y][x][z] + 1
                        q.append((ny, nx, z+1))

    
    return -1

print(bfs(0, 0, 0))