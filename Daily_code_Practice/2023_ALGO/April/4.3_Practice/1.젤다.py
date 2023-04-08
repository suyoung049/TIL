import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

INF = sys.maxsize

def dijkstra(y, x):
    zelda = []
    dp[y][x] = matrix[y][x]
    heappush(zelda, (dp[y][x], y, x))

    while zelda:
        (money, y, x) = heappop(zelda)

        if dp[y][x] < money:
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx <n:
                n_money = money + matrix[ny][nx]

                if n_money < dp[ny][nx]:
                    dp[ny][nx] = n_money
                    heappush(zelda, (dp[ny][nx], ny, nx))

i = 0
while True:
    n = int(input())
    i += 1

    if n == 0:
        break

    else:
        matrix = [list(map(int, input().split())) for _ in range(n)]
        dp = [[INF]*n for _ in range(n)]

        dijkstra(0, 0)
        print(f"Problem {i}: {dp[n-1][n-1]}")
        



