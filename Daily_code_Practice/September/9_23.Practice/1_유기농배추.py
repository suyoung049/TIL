import sys
from collections import deque
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

def pprint(list_):
    for row in list_:
        print(row)

T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())

    matrix = [[0]*m for _ in range(n)]
    check = [[False]*m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        matrix[y][x] = 1

    def bfs(y, x):
        q = deque([(y,x)])

        while q:
            y, x = q.popleft()

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0<= ny < n and 0<= nx < m and check[ny][nx] == False:
                    if matrix[ny][nx] == 1:
                        check[ny][nx] = True
                        q.append((ny,nx))
    count = 0
    for j in range(n):
        for i in range(m):
            if matrix[j][i] == 1 and check[j][i] == False:
                check[j][i] = True
                count += 1
                bfs(j,i)

    print(count)                   