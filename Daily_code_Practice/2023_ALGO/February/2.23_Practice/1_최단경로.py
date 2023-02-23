import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline
from heapq import heappush, heappop

inf = sys.maxsize

n, m = map(int, input().split())

start = int(input())

graph = [[] for _ in range(n+1)]
dp = [inf for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))


def dijkstra(start):
    heap = []
    dp[start] = 0
    heappush(heap, (0,start))

    while heap:
        y, x = heappop(heap)

        if dp[x] < y:
            continue

        for nx, length in graph[x]:
            n_length = y + length
            if dp[nx] > n_length:
                dp[nx] = n_length
                heappush(heap, (n_length, nx))

dijkstra(start)

for i in range(1,n+1):
    if dp[i] == inf:
        print('INF')
    else:
        print(dp[i])
