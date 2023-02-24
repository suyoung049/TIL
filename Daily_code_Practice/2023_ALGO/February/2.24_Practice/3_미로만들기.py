import sys
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline
from heapq import heappop, heappush

n = int(input())
inf = sys.maxsize

dy = [0, 1, -1, 0]
dx = [1, 0, 0, -1]

matrix = [list(map(int, input().strip())) for _ in range(n)]
check = [[inf]*n for _ in range(n)]


def dijkstra():
    heqp = []
    heappush(heqp, (0, 0, 0))
    check[0][0] = 0

    while heqp:
        z, y, x = heappop(heqp)

        if check[y][x] < z:
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0<= nx < n and check[ny][nx] == inf:
                if matrix[ny][nx] == 1:
                    n_cost = z
                else:
                    n_cost = z + 1

                if check[ny][nx] > n_cost:
                    check[ny][nx] = n_cost
                    heappush(heqp, (n_cost, ny,nx))
 
dijkstra()
print(check[n-1][n-1])