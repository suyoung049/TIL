import sys
from collections import deque
sys.stdin = open("1_input.txt","r")
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

n, m, g, r = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

def bfs(seed_li):
    flower = 0
    check = [[0] * m for _ in range(n)]
    q = deque()

    for i in range(T_garden):
        if seed_li[i] == 0:
            continue
       
        y, x = garden_li[i][0], garden_li[i][1]
        q.append((y,x))
        check[y][x] = seed_li[i]
        
    while q:
        y, x = q.popleft()
        if check[y][x] == 2500:
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0<= nx < m and matrix[ny][nx] != 0 and check[ny][nx] != 2500:
                if check[y][x] < 0:
                    if check[ny][nx] + (check[y][x] - 1) == 0:
                        check[ny][nx] = 2500
                        flower += 1
                    
                    elif check[ny][nx] == 0:
                        check[ny][nx] = check[y][x] - 1
                        q.append((ny, nx))
                
                elif check[y][x] > 0:
                    if check[ny][nx] + (check[y][x] + 1) == 0:
                        check[ny][nx] = 2500
                        flower += 1
                    
                    elif check[ny][nx] == 0:
                        check[ny][nx] = check[y][x] + 1
                        q.append((ny,nx))
    return flower
      
def dfs(tc, gc, rc, seed_li):
    global answer
    if tc == T_garden:
        if gc == g and rc == r:
            result = bfs(seed_li)
            answer = max(answer, result)
        return
    
    dfs(tc+1, gc+1, rc, seed_li + [1])
    dfs(tc+1, gc, rc+1, seed_li + [-1])
    dfs(tc+1, gc, rc, seed_li + [0])


garden_li = []

for j in range(n):
    for i in range(m):
        if matrix[j][i] == 2:
            garden_li.append((j, i))

T_garden = len(garden_li)

answer = 0
dfs(0, 0, 0, [])

print(answer)