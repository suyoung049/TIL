import sys
from collections import deque
sys.stdin = open("2_input.txt", "r")
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]


def bfs(y, x):
    q = deque([(y,x)])
    dp[y][x] += 1


    while q:
        y, x = q.popleft()

        if (y, x) == (n-1, m-1):
            return
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0<=nx < m:
                if matrix[y][x] > matrix[ny][nx]:
                    dp[ny][nx] = dp[y][x] + 1
                    q.append((ny, nx))

bfs(0, 0)
pprint(dp)