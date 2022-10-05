import sys
from collections import deque
from itertools import combinations
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline
def pprint(list_):
    for row in list_:
        print(row)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

virous = []
count = 0

for j in range(n):
    for i in range(n):
        if matrix[j][i] == 2:
            virous.append([j,i])
            count += 1
        elif matrix[j][i] == 0:
            count += 1

result = sys.maxsize
count -= m



for com_ in combinations(virous, m):
    check = [[-1] * n for _ in range(n)]
    q= deque()
    min_count = count
    max_time = 0
    
    for e in com_:
        q.append(e)
        check[e[0]][e[1]] = 0

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0<= nx <n and matrix[ny][nx] != 1:
                if check[ny][nx] == -1:
                    check[ny][nx] = check[y][x] + 1
                    q.append([ny, nx])
                    min_count -= 1
    
   
    max_time = check[y][x]
    
    if min_count == 0:
        result = min(max_time, result)
if result == sys.maxsize:
    print(-1)
else:
    print(result)



    







