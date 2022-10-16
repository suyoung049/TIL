from collections import deque
import sys
sys.stdin = open('9_input.txt')
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

def bfs():

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and matrix[ny][nx] != '#':
                if matrix[ny][nx] == '.' and matrix[y][x] == 'J':
                    matrix[ny][nx] = 'J'
                    check[ny][nx] = check[y][x] + 1
                    q.append((ny, nx))

                elif (matrix[ny][nx] == '.' or matrix[ny][nx] == 'J') and matrix[y][x] =='F':
                    matrix[ny][nx] = 'F'
                    q.append((ny,nx))


for j in range(n):
    for i in range(m):
        if matrix[j][i] == 'J':
            check[j][i] = 1
            q.append((j,i))

for j in range(n):
    for i in range(m):
        if matrix[j][i] == 'F':
            q.append((j,i))

bfs()

pprint(check)
min_value = int(1e9)

for i in range(m):
    if check[0][i] != 0:
        min_value = min(check[0][i], min_value)
    if check[n-1][i] != 0:  
        min_value = min(check[n-1][i], min_value) 

for j in range(n):
    if check[j][0] != 0:
        min_value = min(check[j][0], min_value)
    if check[j][m-1] != 0:     
        min_value = min(check[j][m-1], min_value) 

if min_value == int(1e9):
    print("IMPOSSIBLE")

else:
    print(min_value)