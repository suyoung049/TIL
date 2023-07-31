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
    
    dir, khan = map(int, input().split())
    move_cloud = []

    for y, x in cloud:

        ny = ((y + (dy[dir] * khan) + n)  % n)
        nx = ((x + (dx[dir] * khan) + n)  % n)

        matrix[ny][nx] += 1
       
        move_cloud.append((ny, nx))
    
    for ny, nx in move_cloud:
        
        for i in range(4):
            diagonal_y = ny + di_y[i]
            diagonal_x = nx + di_x[i]

            if 0<= diagonal_y < n and 0 <= diagonal_x < n:
                if matrix[diagonal_y][diagonal_x] > 0:
                    matrix[ny][nx] += 1

    temp = []
    for j in range(n):
        for i in range(n):
            if (j, i) not in move_cloud:
                if matrix[j][i] >= 2:
                    temp.append((j, i))
                    matrix[j][i] -= 2
            
    
    cloud = temp

answer = 0

for j in range(n):
    for i in range(n):
        answer += matrix[j][i]

print(answer)