import sys
sys.stdin = open('1_input.txt', 'r')
from collections import deque
input = sys.stdin.readline

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def pprint(list_):
    for row in list_:
        print(row)

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
temp = [[0] *m for _ in range(n)]


count = 0

def bfs(y,x):
    q = deque([(y,x)])

    




for j in range(n):
    for i in range(m):
        
        if map[j][i] != 0:
            stack = 0
            
            for k in range(4):
                ny = j + dy[k]
                nx = i + dx[k]

                if map[ny][nx] == 0:
                    stack += 1
            
            temp[j][i] = map[j][i] - stack
            if temp[j][i] < 0:
                temp[j][i] = 0

ice = 0
check = [[False]*m for _ in range(n)]
for y in range(n):
    for x in range(m):
        if temp[y][x] != 0 and not check:
            bfs(y,x)
            ice += 1
            
