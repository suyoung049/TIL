import sys
from collections import deque
from itertools import combinations
sys.stdin = open('1_input.txt','r')
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def pprint(list_):
    for row in list_:
        print(row)

n, m = map(int, input().split())

matrix = [list(map(int, input().split()))for _ in range(n)]

def bfs(y,x,check):
    q = deque([(y,x)])
    kill_check = True
    ston = 1

    while q:
        y,x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny<n and 0<= nx < m and not check[ny][nx]:
                if matrix[ny][nx] == 0:
                    kill_check = False
                elif matrix[ny][nx] == 2:
                    check[ny][nx] = True
                    ston += 1
                    q.append((ny,nx))
    
    if kill_check == False:
        return -1
    else:
        return ston

def play(combi):
    check = [[False]*m for _ in range(n)]
    kill = 0
    for y,x in combi:
        matrix[y][x] = 1

    for j in range(n):
        for i in range(m):
            if matrix[j][i] == 2 and not check[j][i]:
                check[j][i] = True
                result = bfs(j,i,check)

                if result != -1:
                    kill += result
    
    for y,x in combi:
        matrix[y][x] = 0
    
    return kill

blank = []
for j in range(n):
    for i in range(m):
        if matrix[j][i] == 0:
            blank.append((j,i))

max_ston = 0

for combi in combinations(blank, 2):
    max_ston = max(max_ston, play(combi))

print(max_ston)
