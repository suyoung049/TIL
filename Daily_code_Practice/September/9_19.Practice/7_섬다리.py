import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
sys.stdin = open('7_input.txt', 'r')
input = sys.stdin.readline

dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

def pprint(list_):
    for row in list_:
        print(row)

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]
check = [[0] *n for _ in range(n)]
bridge = sys.maxsize


def dfs(y, x, c):
    matrix[y][x] = c
    check[y][x] = 1
   

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0<= nx < n and check[ny][nx] == 0:
            if matrix[ny][nx] == 1:
                dfs(ny,nx,c)

def bfs(c):
    global bridge
    check = [[0] *n for _ in range(n)]
    q = deque()

    for j in range(n):
        for i in range(n):
            if matrix[j][i] == c:
                q.append((j,i))
                check[j][i] = 1
                
    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0<= nx < n:
                if matrix[ny][nx] > 0 and matrix[ny][nx] != c:
                    bridge = min(bridge, check[y][x]-1)
                    return
                if check[ny][nx] == 0 and matrix[ny][nx] == 0:
                    check[ny][nx] = check[y][x] + 1
                    q.append((ny,nx))
            

        
count = 0
for j in range(n):
    for i in range(n):
        if matrix[j][i] == 1 and check[j][i] == 0:
            count += 1
            dfs(j, i, count)


pprint(matrix)
for i in range(1,count+1):
    bfs(i)
print(bridge)