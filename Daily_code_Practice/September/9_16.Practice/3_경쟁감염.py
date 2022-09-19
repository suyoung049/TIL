import sys
from collections import deque
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

def pprint(list_):
    for row in list_:
        print(row)

n , m  = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
virous = []

s, y, x = map(int,input().split())

for j in range(n):
    for i in range(n):
        if matrix[j][i] != 0:
            virous.append((matrix[j][i], j, i))

virous.sort()
print(virous)

def bfs(s):
    count = 0
    q = deque(virous)

    while q:
        if count == s:
            break

        for _ in range(len(q)):
            v, y, x = q.popleft()

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0<= ny < n and 0<= nx <n:
                    if matrix[ny][nx] == 0:
                        matrix[ny][nx] = v
                        q.append((matrix[ny][nx], ny, nx))
                        
        count += 1
bfs(s)

if matrix[y-1][x-1] == 0:
    print(0)
else:
    print(matrix[y-1][x-1])

        



