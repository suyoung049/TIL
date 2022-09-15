import sys 
from collections import deque
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

def pprint(list_):
    for row in list_:
        print(row)


n, k = map(int,input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
virous = []


for j in range(n):
    for i in range(n):
        if matrix[j][i] != 0:
            virous.append((matrix[j][i], j, i))

virous.sort()

s, y, x = map(int, input().split())

def bfs(s):
    q = deque(virous)
    count = 0

    while q:
        if count == s:
            break
        for _ in range(len(q)):  # 첫 시작을 여러곳에서 시작할 때 응용
            v, y, x = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0<= ny < n and 0<= nx <n:
                    if matrix[ny][nx] == 0:
                        matrix[ny][nx] = matrix[y][x]
                        q.append((matrix[ny][nx], ny, nx))
        count += 1

bfs(s)
pprint(matrix)
      
if matrix[y-1][x-1] == 0:
    print(0)
else:
    print(matrix[y-1][x-1])

