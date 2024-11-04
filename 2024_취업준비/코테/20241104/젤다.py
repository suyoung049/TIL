import sys
from heapq import heappop, heappush
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

INF = float('inf')
p_num = 0
while True:
    p_num += 1
    n = int(input())

    if not n:
        break

    matrix = [list(map(int, input().split())) for _ in range(n)]
    dp = [[INF for _ in range(n)] for _ in range(n)]
    dp[0][0] = matrix[0][0]
    queue = []

    heappush(queue, (matrix[0][0], 0, 0))

    while queue:
        cost, y, x = heappop(queue)

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n:
                n_cost = cost + matrix[ny][nx]
                if dp[ny][nx] > n_cost:
                    dp[ny][nx] = n_cost
                    heappush(queue, (dp[ny][nx], ny, nx)) 
    
    print(f"Problem {p_num}: {dp[n-1][n-1]}")






