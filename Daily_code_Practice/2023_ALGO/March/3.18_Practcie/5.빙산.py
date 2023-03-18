import sys
sys.setrecursionlimit(10**5)
sys.stdin = open('5_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

year = 0

def dfs(y, x):
    check[y][x] = True

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        if 0 <= ny < n and 0 <= nx < m and not check[ny][nx]:
            if temp[ny][nx] != 0:
                dfs(ny, nx)

while True:
    temp = [[0]*m for _ in range(n)]
    for j in range(n):
        for i in range(m):
            if matrix[j][i] != 0:

                water = 0

                for k in range(4):
                    ny = j + dy[k]
                    nx = i + dx[k]

                    if matrix[ny][nx] == 0:
                        water += 1
                
                temp[j][i] = matrix[j][i] - water

                if temp[j][i] < 0:
                    temp[j][i] = 0

    year += 1

    ice_count = 0
    check = [[False] * m for _ in range(n)]
    
    for j in range(n):
        for i in range(m):
            if temp[j][i] !=0 and not check[j][i]:
                dfs(j, i)
                ice_count += 1

    solving = False
    
    if ice_count > 1:
        break
    
    else:
        for j in range(n):
            for i in range(m):
                matrix[j][i] = temp[j][i]
                if matrix[j][i] !=0:
                    solving = True

    
    if solving == False:
        year = 0
        break

print(year)
    



                


