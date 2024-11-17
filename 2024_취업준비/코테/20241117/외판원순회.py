import sys
from heapq import heappop, heappush
sys.stdin = open('2_input.txt', 'r')

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]


INF = float('inf')

def tsp():
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0  # 시작점을 0번 도시로 고정

    for state in range(1 << n):
        for u in range(n):
            if dp[state][u] == INF:
                continue
            for v in range(n):
                if state & (1 << v):
                    continue
                if matrix[u][v] == 0:
                    continue
                next_state = state | (1 << v)
                if dp[next_state][v] > dp[state][u] + matrix[u][v]:
                    dp[next_state][v] = dp[state][u] + matrix[u][v]

    ans = INF
    for i in range(n):
        if matrix[i][0] == 0:
            continue
        ans = min(ans, dp[(1 << n) - 1][i] + matrix[i][0])

    return ans

print(tsp())

