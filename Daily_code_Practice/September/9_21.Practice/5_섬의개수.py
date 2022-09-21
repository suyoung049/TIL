import sys
from collections import deque
sys.stdin = open('5_input.txt', 'r')
input = sys.stdin.readline

dy = [0, 1, 0, -1, 1, -1, 1, -1]
dx = [1, 0, -1, 0, 1, 1, -1, -1]

def pprint(list_):
    for row in list_:
        print(row)

while True:
    n, m = map(int, input().split())
    if (n,m) == (0,0):
        break

    else:
        matrix = [list(map(int, input().split())) for _ in range(m)]
        check = [[False] * n for _ in range(m)]

        def bfs(y,x):
            q = deque([(y,x)])

            while q:
                y,x = q.popleft()

                for i in range(8):
                    ny = y + dy[i]
                    nx = x + dx[i]

                    if 0<=ny<m and 0<=nx<n and check[ny][nx] == False:
                        if matrix[ny][nx] == 1:
                            check[ny][nx] = True
                            q.append((ny,nx))
        count = 0
        for j in range(m):
            for i in range(n):
                if matrix[j][i] == 1 and check[j][i] == False:
                    count += 1
                    bfs(j,i)
        
        print(count)
