import sys
sys.stdin = open('2_input.txt', 'r')
from collections import deque
input = sys.stdin.readline

dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

def pprint(list_):
    for row in list_:
        print(row)

n, m, k = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]     
check = [[0] * m for _ in range(n)]

def bfs(y,x):
    sowrd = sys.maxsize
    q = deque([(y,x)])
    
    while q:
        y,x = q.popleft()

        if (y, x) == (n-1, m-1):
            return min(sowrd, check[y][x])

        if matrix[y][x] == 2:
            sowrd = check[y][x] + (n-1-y) + (m-1-x)

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0<= nx < m and check[ny][nx] == 0:
                if matrix[ny][nx] == 0 or matrix[ny][nx] == 2:
                    check[ny][nx] = check[y][x] + 1
                    q.append((ny,nx))
    
    

result = bfs(0, 0)

if not result:
    print('Fail')
else:
    if result < k:
        print(result)
    else:
        print('Fail')


