import sys
from collections import deque
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

dy = [1, 0]
dx = [0, 1]

def pprint(list_):
    for row in list_:
        print(row)

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]
check = [[] * n for _ in range(n)]
dp = [[0] * n for _ in range(n)]


def bfs(y,x):
    q = deque([(y,x)])

    while q:
        y, x = q.popleft()
        if (y, x) == (n-1, n-1):
            continue

        jump = matrix[y][x]

        for i in range(2):
            ny = y + (dy[i] * jump)
            nx = x + (dx[i] * jump)
            

            if ny < n and nx < n:
                dp[ny][nx] += 1
                q.append((ny,nx))

bfs(0,0)
pprint(dp)
print(dp[n-1][n-1])