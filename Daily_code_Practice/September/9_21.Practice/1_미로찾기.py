import sys
from collections import deque
sys.stdin = open('1_input.txt')
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def pprint(list_):
    for row in list_:
        print(row)

n, m = map(int, input().split())

matrix = [list(map(int, input().strip())) for _ in range(n)]
check = [[0]*m for _ in range(n)]

def bfs():
    
    q = deque([(0,0)])
    check[0][0] = 1

    while q:
        y, x = q.popleft()
        
        if (y, x) == (n-1, m-1):
            return (check[y][x])

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny <n and 0 <= nx < m and check[ny][nx] == 0:
                if matrix[ny][nx] == 1:
                    check[ny][nx] = check[y][x] + 1
                    
                    q.append((ny,nx))

print(bfs())



