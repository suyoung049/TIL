import sys
from collections import deque
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def pprint(list_):
    for row in list_:
        print(row)


n, m = map(int, input().split())

matrix = [list(input().strip()) for _ in range(n)]
walk_check = [[0] * m for _ in range(n)]
fire_check = [[False] * m for _ in range(n)]


def bfs(q, walk_check, fire_check):
    
    while q:
        y, x, state = q.popleft()

        if (y == n - 1 or x == m - 1 or y == 0 or x == 0) and matrix[y][x] != 'F' and state == 'J':
                return walk_check[y][x] + 1
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0 <=nx < m:
                
                if matrix[ny][nx] == '.' and not walk_check[ny][nx] and state == 'J' and matrix[y][x] != 'F':
                    walk_check[ny][nx] = walk_check[y][x] + 1
                    q.append((ny, nx, 'J')) 
                    
                elif matrix[ny][nx] != '#' and not fire_check[ny][nx] and state =='F':
                    matrix[ny][nx] = 'F'
                    fire_check[ny][nx] = True
                    q.append((ny,nx,'F'))
    
q = deque()

for j in range(n):
    for i in range(m):
        if matrix[j][i] == 'J':
            q.append((j, i, 'J'))

for j in range(n):
    for i in range(m):
        if matrix[j][i] == 'F':
            fire_check[j][i] = True
            q.append((j,i,'F'))


result = (bfs(q, walk_check, fire_check))

if result:
    print(result)
else:
    print('IMPOSSIBLE')




