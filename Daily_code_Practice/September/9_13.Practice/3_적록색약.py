import sys
from collections import deque
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

dy = [0, 1, 0, -1]
dx = [1 ,0, -1, 0]

n = int(input())

matrix = [list(input().strip()) for _ in range(n)]
check = [[False]*n for _ in range(n)]

def bfs_r(y,x):
    q = deque([(y,x)])

    while q:
        y,x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0<= nx < n:
                if matrix[ny][nx] == 'R' and check[ny][nx] == False:
                    check[ny][nx] = True
                    q.append((ny,nx))

def bfs_g(y,x):
    q = deque([(y,x)])

    while q:
        y,x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0<= nx < n:
                if matrix[ny][nx] == 'G' and check[ny][nx] == False:
                    check[ny][nx] = True
                    q.append((ny,nx))

def bfs_b(y,x):
    q = deque([(y,x)])

    while q:
        y,x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0<= nx < n:
                if matrix[ny][nx] == 'B' and check[ny][nx] == False:
                    check[ny][nx] = True
                    q.append((ny,nx))



count_1 = 0
for j in range(n):
    for i in range(n):
        if matrix[j][i] == 'R' and check[j][i] == False:
            count_1 += 1
            check[j][i] = True
            bfs_r(j,i)
        
        if matrix[j][i] == 'G' and check[j][i] == False:
            count_1 += 1
            check[j][i] = True
            bfs_g(j,i)
        
        if matrix[j][i] == 'B' and check[j][i] == False:
            count_1 += 1
            check[j][i] = True
            bfs_b(j,i)

for j in range(n):
    for i in range(n):
        if matrix[j][i] == 'G':
            matrix[j][i] = 'R'

check = [[False]*n for _ in range(n)]

count_2 = 0
for j in range(n):
    for i in range(n):
        if matrix[j][i] == 'R' and check[j][i] == False:
            count_2 += 1
            check[j][i] = True
            bfs_r(j,i)
        
        if matrix[j][i] == 'B' and check[j][i] == False:
            count_2 += 1
            check[j][i] = True
            bfs_b(j,i)


print(count_1, count_2)

