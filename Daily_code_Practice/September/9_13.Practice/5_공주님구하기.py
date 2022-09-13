import sys
from collections import deque
sys.stdin = open('5_input.txt', 'r')
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def pprint(list_):
    for row in list_:
        print(row)

n, m , k = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
visit = [[-1] *m for _ in range(n)]

def bfs():
    
    soward = sys.maxsize
    q = deque([(0,0)])
    visit[0][0] = 0

    while q:
        y, x = q.popleft()

        if (y,x) == (n-1,m-1):

            return  min(visit[y][x], soward)

        if matrix[y][x] == 2:
            soward = (visit[y][x]) + (n-1-y) + (m-1-x)

        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0<= nx < m and visit[ny][nx] == -1:
                if matrix[ny][nx] == 0 or matrix[ny][nx] == 2:
                    visit[ny][nx] = visit[y][x] + 1
                    q.append((ny,nx))
    return soward

result = bfs()

if result > k:
    print('Fail')
else:
    print(result)



                    

        




