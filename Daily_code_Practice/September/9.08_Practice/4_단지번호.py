import sys
from collections import deque
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

n = int(input())

matrix = [list(map(int, input().strip())) for _ in range(n)]
check = [[False]*n for _ in range(n)]

def dfs(y,x):
    size = 1
    q = deque([(y,x)])
    check[y][x] = True

    while q:

        y,x = q.popleft()

        for i in range(4):

            ny = y + dy[i]
            nx = x + dx[i]

            if 0<=ny<n and 0<=nx<n:
                if matrix[ny][nx] == 1 and check[ny][nx] == False:
                    check[ny][nx] = True
                    size += 1
                    q.append((ny,nx))
    return size                

count = 0
ground = []

for j in range(n):
    for i in range(n):

        if matrix[j][i] == 1 and check[j][i] == False:
            check[j][i] = True
            count += 1
            ground.append(dfs(j,i))

sr_ground = sorted(ground)            

print(count)
for i in sr_ground:
    print(i)