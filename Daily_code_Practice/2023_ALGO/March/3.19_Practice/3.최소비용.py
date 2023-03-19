import sys
from heapq import heappop, heappush
sys.stdin = open('3_input.txt','r')
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = sys.maxsize

graph = [[] for _ in range(n+1)]
cost = [INF] * (n+1)


for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

start, end = map(int, input().split())


heapque = []
def dijkstra(start):
    heappush(heapque, (start, 0))
    cost[start] = 0

    while heapque:
        y, line_cost = heappop(heapque)

        if cost[y] < line_cost:
            continue

        for i in graph[y]:
            sum_cost = line_cost + i[1]


            if cost[i[0]] > sum_cost:
                cost[i[0]] = sum_cost
                heappush(heapque, (i[0], sum_cost))

dijkstra(start)
print(cost[end])





