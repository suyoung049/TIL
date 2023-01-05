import sys
sys.stdin = open('2_input.txt', 'r')
from collections import deque
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

dy = [0, 1, -1, 0]
dx = [1, 0, 0, -1]

n, k = map(int, input().split())
virous = []

matrix = list(list(map(int, input().split())) for _ in range(n))

z, y, x = map(int, input().split())

for j in range(n):
    for i in range(n):
        if matrix[j][i] != 0:
            virous.append((matrix[j][i], j, i))

virous.sort()


def bfs(z):
    count = 0
    q = deque(virous)

    while q:
        if count == z:
            break

        for _ in range(len(q)):
            v, y, x = q.popleft()

            for i in range(4):
                
                ny = y + dy[i]
                nx = x + dx[i]

                if 0<= ny < n and 0<= nx < n:
                    if matrix[ny][nx] == 0:
                        matrix[ny][nx] = v
                        q.append((v, ny, nx))
        
        count += 1

bfs(z)

if matrix[y-1][x-1] == 0:
    print(0)
else:
    print(matrix[y-1][x-1])





            




    




