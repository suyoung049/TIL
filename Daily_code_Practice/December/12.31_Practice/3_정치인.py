import sys
sys.stdin = open('3_input.txt', 'r')
from heapq import heappop, heappush
input = sys.stdin.readline
inf = sys.maxsize

def dijk(s):
    dist[s] = 0
    heap = []
    heappush(heap, [0,s])
    path[s] = [s]

    while heap:
        d, now = heappop(heap)

        for x in graph[now]:
            cost = d + x[1]

            if cost < dist[x[0]]:
                dist[x[0]] = cost
                path[x[0]] = path[now] + [x[0]]
                heappush(heap, [cost, x[0]])

T = int(input())

for test_case in range(1, T+1):
    n, m = map(int, input().split())

    graph = [[] for _ in range(m)]
    path = [[] for _ in range(m)]

    for _ in range(n):
        a, b, c = map(int, input().split())
        graph[a].append([b,c])
        graph[b].append([a,c])

    dist = [inf for _ in range(m)]
    dijk(0)

    print(f'Case #{test_case}:', end =' ')

    if path[-1]:
        for i in path[-1]:
            print(i, end = ' ')
    
    else:
        print(-1)
    
    print()





    




