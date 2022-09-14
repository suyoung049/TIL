import sys
from collections import deque
sys.stdin = open('7_input.txt', 'r')
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

def pprint(list_):
    for row in list_:
        print(row)

n , m = map(int,input().split())

matrix = [list(map(int,input().split())) for _ in range(m)]
q = deque([])

for j in range(m):
    for i in range(n):
        if matrix[j][i] == 1:
            q.append((j,i))
        

def bfs():
    
    while q:
        ey,ex = q.popleft()

        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]

            if 0<= ny < m and 0<= nx <n:
                if matrix[ny][nx] == 0:
                    matrix[ny][nx] = matrix[ey][ex] + 1
                    q.append((ny,nx))


bfs()
            
pprint(matrix)

max_ = 0
check = True
for k in range(m):
    for l in range(n):
        if matrix[k][l] == 0:
            check = False
            break
        else:
            max_ = max(max_ , (matrix[k][l]-1))

if check == False:
    print(-1)

else:
    print(max_)
            