import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

m, n = map(int, input().split())
k = int(input())

matrix = [[0] * m for _ in range(n)]

if k == 1:
    print(1, 1)

else:
    y, x = 0, 0
    matrix[y][x] = 1
    dir = 0
    for i in range(2, (m*n) + 1):
        if k > m * n:
            print(0)
            break

        ny = y + dy[dir]
        nx = x + dx[dir]

        if 0<= ny < n and 0<= nx < m and matrix[ny][nx] == 0:
            matrix[ny][nx] = i
        
        else:
            dir = (dir+1) % 4
            ny = y + dy[dir]
            nx = x + dx[dir]
            
            matrix[ny][nx] = i
        
        y = ny
        x = nx

        if i == k:
            print(nx+1, ny+1)
            


        
