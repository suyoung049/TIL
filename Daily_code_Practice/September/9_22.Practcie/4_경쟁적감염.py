import sys
from collections import deque
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

def pprint(list_):
    for row in list_:
        print(row)

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

a, b, c = map(int, input().split())
check = [[False] *m for _ in range(n)]
virous = []

for j in range(n):
    for i in range(m):
        if matrix[j][i] != 0:
            virous.append((matrix[j][i], j, i))

virous.sort()

def bfs(s):
    count = 0
    q = deque(virous)

    while q:
        if count == s:
            break

        for _ in range(len(virous)):
            v, y, x = q.popleft()

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0<= ny < n and 0<= nx < m and check[ny][nx] == False:
                    if matrix[ny][nx] == 0:
                        check[ny][nx] = True
                        matrix[ny][nx] = v
                        q.append((matrix[ny][nx], ny, nx))
        
        count += 1

bfs(a)

print(matrix[b-1][c-1])



