import sys
import copy
from collections import deque
sys.stdin = open('8_input.txt', 'r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

result = 0
q = deque()

def bfs():
    global result
     
    matix_c = [[0] *m for _ in range(n)]
    check = [[False] * m for _ in range(n)]

    for j in range(n):
        for i in range(m):
            matix_c[j][i] = matrix[j][i]
    
    for j in range(n):
        for i in range(m):
            if matix_c[j][i]==2:
                check[j][i] = True
                q.append((j,i))

    while q:
        y,x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny <n and 0<= nx < m and check[ny][nx] == False:
                if matix_c[ny][nx] == 0:
                    check[ny][nx] = True
                    matix_c[ny][nx] = 2
                    q.append((ny,nx))
    
    answer = 0
    for i in matix_c:
        answer += i.count(0)
        result = max(result, answer)



def wall(x):
    if x == 3:
        bfs()
        return

    for j in range(n):
        for i in range(m):
            if matrix[j][i] == 0:
                matrix[j][i] = 1
                wall(x+1)
                matrix[j][i] = 0

wall(0)
print(result)
