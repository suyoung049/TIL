import sys
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline
from heapq import heappop, heappush

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

inf = sys.maxsize

def pprint(list_):
    for row in list_:
        print(row)


n, m = map(int, input().split())

matrix = [list(map(int, input().strip())) for _ in range(m)]
dp = [[inf]*n for _ in range(m)]



def dijkstra():
    heap = []
    heappush(heap, (0,0,0))
    dp[0][0] = 0

    while heap:
        z, y, x = heappop(heap)

        if dp[y][x] < z:
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < m and 0<= nx < n and dp[ny][nx] == inf:
                n_cost = z + matrix[ny][nx]
                if dp[ny][nx] > n_cost:
                    dp[ny][nx] = n_cost
                    heappush(heap, (n_cost, ny, nx))

dijkstra()
print(dp[m-1][n-1])