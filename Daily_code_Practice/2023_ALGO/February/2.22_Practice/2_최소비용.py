import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline
from heapq import heappush, heappop

n = int(input())
m = int(input())

inf = sys.maxsize

grap = [[] for _ in range(n+1)]
check = [inf for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    grap[a].append((b,c))


start, end = map(int, input().split())


def dijkstra(start):
    check[start] = 0
    bus = []
    heappush(bus, (0,start))

    while bus:
        y,x = heappop(bus)

        if check[x] < y:
            continue

        for nx, cost in grap[x]:
            n_cost = y + cost

            if check[nx] > n_cost:
                check[nx] = n_cost
                heappush(bus, (n_cost, nx))

dijkstra(start)
print(check[end])

