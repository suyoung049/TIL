import sys
sys.stdin = open("2_input.txt", "r")
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]

di_y = [1, 1, -1, -1]
di_x = [1, -1, -1, 1]
 
n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

cloud = [(n-1,0), (n-1,1), (n-2,0), (n-2, 1)]

for _ in range(m):
    check = [[False] * n for _ in range(n)]
    dir, khan = map(int, input().split())

    for y, x in cloud:

        ny = ((y + (dy[dir] * khan) + 5)  % 5)
        nx = ((x + (dx[dir] * khan) + 5)  % 5)

        matrix[ny][nx] += 1
        check[ny][nx] = True

        for i in range(4):
            diagonal_y = ny + di_y[i]
            diagonal_x = nx + di_x[i]

            if 0<= diagonal_y < n and 0 <= diagonal_x < n:
                if matrix[diagonal_y][diagonal_x] != 0:
                    matrix[ny][nx] += 1

    temp = []
    for j in range(n):
        for i in range(n):
            if not check[j][i] and matrix[j][i] >= 2:
                temp.append((j, i))
                matrix[j][i] -= 2
    
    cloud = temp



pprint(matrix)