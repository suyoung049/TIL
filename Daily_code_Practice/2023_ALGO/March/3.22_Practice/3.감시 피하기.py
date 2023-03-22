import sys
sys.stdin = open('3_input.txt', 'r')
from collections import deque
from itertools import combinations
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

n = int(input())

school = [list(input().split()) for _ in range(n)]

def bfs():
    watch = True
    check = [[False] * n for _ in range(n)]
    
    q = deque()
    for j in range(n):
        for i in range(n):
            if school[j][i] == 'T':
                check[j][i] = True
                q.append((j,i))

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0<= nx < n and not check[ny][nx] and school[ny][nx] != 'O':
                if school[ny][nx] == 'S':
                    watch = False
                    break

                elif school[ny][nx] == 'X':
                    check[ny][nx] = True
                    if (ny == n - 1 or nx == n - 1 or ny == 0 or nx == 0):
                        continue
                    else:
                        q.append((ny, nx))

    
    return watch

empty_li = []
for j in range(n):
    for i in range(n):
        if school[j][i] == 'X':
            empty_li.append((j,i))

answer = 0
for wall in combinations(empty_li, 3):
    for w in wall:
        school[w[0]][w[1]] = 'O'
    
    watch = bfs()

    if watch == True:
        answer = 1
        break

    for w in wall:
        school[w[0]][w[1]] = 'X'

if answer == 1:
    print('YES')
else:
    print('NO')





    
