import sys
sys.stdin = open("1_input.txt", "r")
sys.setrecursionlimit(10 ** 4)
from collections import deque
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def pprint(list_):
    for row in list_:
        print(row)

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]
check = [[False] * n for _ in range(n)]


def dfs(y, x, num_):
    matrix[y][x] = num_
   
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0<= ny < n and 0<= nx <n and not check[ny][nx]:
            if matrix[ny][nx] == 1:
                check[ny][nx] = True
                dfs(ny, nx, num_)


def bfs(s):
    bridge = sys.maxsize

    check = [[0] * n for _ in range(n)]
    q = deque()

    for j in range(n):
        for i in range(n):
            if matrix[j][i] == s:
                q.append((j,i))
    
    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0<= nx < n:
                if matrix[ny][nx] > 0 and matrix[ny][nx] != s:
                    bridge = min(bridge, check[y][x])
                    
                    
                if matrix[ny][nx] == 0 and check[ny][nx] == 0:
                    check[ny][nx] = check[y][x] + 1
                    q.append((ny,nx))
    return bridge
                
island_num = 0
for j in range(n):
    for i in range(n):
        if matrix[j][i] == 1 and not check[j][i]:
            island_num += 1
            dfs(j, i, island_num)

result = sys.maxsize
for i_num in range(1, island_num+1):
    answer = bfs(i_num)
    if result >= answer:
        result = answer

print(result)

    






