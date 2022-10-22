import sys
from collections import deque
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

dy = [-2, -2, 0, 0, 2, 2]
dx = [-1, 1, -2, 2, -1, 1]

def pprint(list_):
    for row  in list_:
        print(row)

n = int(input())

sy, sx, fy, fx = map(int, input().split())

check = [[-1]*n for _ in range(n)]


def bfs(y,x):
    check[y][x] = 0
    q = deque([(y,x)])

    while q:
        y, x = q.popleft()

        if (y, x) == (fy, fx):
            return check[y][x]
        
        for i in range(6):

            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0<= nx <n and check[ny][nx] == -1:
                check[ny][nx] = check[y][x] + 1
                q.append((ny,nx))
    return -1

print(bfs(sy,sx))


