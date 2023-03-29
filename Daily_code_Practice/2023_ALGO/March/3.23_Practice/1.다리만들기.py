import sys
sys.stdin = open('1_input.txt', 'r')
from collections import deque
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def pprint(list_):
    for row in list_:
        print(row)

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]
color_check = [[False] * n for _ in range(n)]
bridge = sys.maxsize


def dfs(y, x, color):
    color_check[y][x] = True
    matrix[y][x] = color

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0<= ny < n and 0<= nx < n and not color_check[ny][nx]:
            if matrix[ny][nx] != 0:
                dfs(ny, nx, color)


def bfs(color):
    global bridge
    move_check = [[0] * n for _ in range(n)]

    q = deque()

    for j in range(n):
        for i in range(n):
            if matrix[j][i] == color:
                q.append((j,i))
    

    while q:

        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0<= nx < n and move_check[ny][nx] == 0:
                if matrix[ny][nx] == 0:
                    move_check[ny][nx] = move_check[y][x] + 1
                    q.append((ny,nx))

                elif matrix[ny][nx] > 0 and  matrix[ny][nx] != color:
                    bridge = min(bridge, move_check[y][x])
                    return

color = 0

for j in range(n):
    for i in range(n):
        if matrix[j][i] != 0 and not color_check[j][i]:
            color += 1
            dfs(j, i, color)



for i in range(1, color+1):
    bfs(i)

print(bridge)


