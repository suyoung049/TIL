import sys
from heapq import heappop, heappush
sys.stdin = open('1_input.txt', 'r')

n, k = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

INF = float('inf')

# 경우의 수 비트마스킹
# 1000(2) = 8
max_state = (1<<n)

print(1<<3)

# 방문 경로에 따른 모든 최소비용 저장할 DP
dp = [[INF for _ in range(n)] for _ in range(max_state)]

# 출발지점의 최소 벼용 0으로 초기화
dp[1<<k][k] = 0

heap = []
heappush(heap, (0, 1<<k, k))

while heap:
    cost, state, j = heappop(heap)

    # j 행성에서 모든 행성 탐사
    for i in range(n):
        # i 번 행성 방문 표시
        next_state = (1<<i) | state
        # i번 행성까지 탐사완료 후 cost
        next_cost = cost + matrix[j][i]
        if dp[next_state][i] > next_cost:
            dp[next_state][i] = next_cost
            heappush(heap, (next_cost, next_state, i))

answer = min(dp[(1<<n)-1])

print(answer)








