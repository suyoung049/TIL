import sys
sys.stdin = open("2_input.txt", "r")
from collections import deque
input = sys.stdin.readline

dy = [0, 1, 0, -1, 0, 0]
dx = [1, 0, -1, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs(y, x, z):
    
    check = [[[0] * c for _ in range(r)] for _ in range(l)]
    q = deque([(y, x, z)])
    check[y][x][z] = 1

    while q:
        y, x, z = q.popleft()

        if build[y][x][z] == "E":
            return check[y][x][z] - 1
            
        
        for i in range(6):
            ny = y + dy[i]
            nx = x + dx[i]
            nz = z + dz[i]

            if 0 <= ny < l and 0 <= nx < r and 0 <= nz <c:
                if build[ny][nx][nz] != "#" and check[ny][nx][nz] == 0:
                    check[ny][nx][nz] = check[y][x][z] + 1
                    q.append((ny, nx, nz))
    
    return "Trapped!"

while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break

    build = []

    for j in range(l):
        store = []
        for i in range(r):
            matrix = list(input().strip())
            store.append(matrix)
        build.append(store)
        if j == l-1:
            break
        else:
            hang = list(input())
            continue
    
    for j in range(l):
        for i in range(r):
            for k in range(c):
                if build[j][i][k] == "S":
                    result = bfs(j, i, k)
    
    if result == "Trapped!":
        print(result)
    else:
        print(f"Escaped in {result} minute(s).")
    hang = input()
    if hang == 'n/':
        continue

    
            


    

    