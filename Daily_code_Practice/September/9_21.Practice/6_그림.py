import sys
sys.stdin = open('6_input.txt', 'r')
from collections import deque
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
check = [[False]*m for _ in range(n)]


def bfs(y,x):
    size = 1
    q = deque([(y,x)])
    check[y][x] = True

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<=ny<n and 0<=nx<m and check[ny][nx] == False:
                if matrix[ny][nx] == 1:
                    check[ny][nx] = True
                    size += 1
                    q.append((ny,nx))
    return size
                    
    

count = 0
result = []
for j in range(n):
    for i in range(m):
        if matrix[j][i] == 1 and check[j][i] == False:
            count += 1
            result.append(bfs(j,i))

print(count)
print(max(result))