import sys
from collections import deque
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def pprint(list_):
    for row in list_:
        print(row)

m, n, k = map(int, input().split())

matrix = [[0]*n for _ in range(m)]
check = [[False]*n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    for j in range(y1, y2):
        for i in range(x1, x2):
            matrix[j][i] = 1

pprint(matrix)

def bfs(y, x):
    size = 1
   
    q = deque([(y,x)])

    while q:
        ey,ex = q.popleft()

        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]

            if 0 <= ny < m and 0 <= nx < n:
                if matrix[ny][nx] == 0 and check[ny][nx] == False:
                    check[ny][nx] = True
                    size += 1
                    q.append((ny,nx))
    return size

count = 0
result = []

for k in range(m):
    for h in range(n):
        if matrix[k][h] == 0 and check[k][h] == False:
            check[k][h] = True
            count +=1 
            result.append(bfs(k,h))

print(count)
result.sort()

for i in result:
    print(i, end = ' ')
