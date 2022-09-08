import sys
from collections import deque
sys.setrecursionlimit(10 ** 6) # 재귀함수의 런타임 오류시 작성 코드 재귀함수 사용시 필수 코드 !!!
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)
dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

n = int(input())

map = [list(map(int, input().split())) for _ in range(n)]
check = [[False]*n for _ in range(n)]

def dfs(y, x, c):
    map[y][x] = c
    check[y][x] = True

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0<=ny<n and 0<=nx<n and check[ny][nx] == False:
            if map[ny][nx] == 1:
                dfs(ny, nx, c)

count = 0
for j in range(n):
    for i in range(n):
        if map[j][i] == 1 and check[j][i] == False:
            count += 1
            dfs (j, i, count) 

pprint(map)