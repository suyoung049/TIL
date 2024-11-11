import sys
from heapq import heappop, heappush
sys.stdin = open('1_input.txt', 'r')

def pprint(matrix):
    for x in matrix:
        print(x)

n = int(input())

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

matrix = [list(map(int, input().strip())) for _ in range(n)]
INF = float('inf')
check = [[INF for _ in range(n)] for _ in range(n)]


heap = []
check[0][0] = 0
heappush(heap, (0, 0, 0))


while heap:

    cost, y, x = heappop(heap)

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < n:
            if matrix[ny][nx] == 1:
                n_cost = cost
            else:
                n_cost = cost + 1

            if check[ny][nx] > n_cost:
                check[ny][nx] = n_cost
                heappush(heap, (n_cost, ny, nx))

print(check[n-1][n-1])
