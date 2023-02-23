import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline
from heapq import heappop, heappush

T = int(input())
inf = sys.maxsize

def dijkstra(strat):
    dp = [inf for _ in range(n+1)]
    heap = []
    dp[strat] = 0
    heappush(heap, (0, strat))

    while heap:
        y,x = heappop(heap)

        if dp[x] < y:
            continue

        for nx,length in graph[x]:
            n_length = length + y

            if dp[nx] > n_length:
                dp[nx] = n_length
                heappush(heap, (n_length, nx))
    return dp

for _ in range(T):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for i in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    
    frind = int(input())

    frind_li = list(map(int, input().split()))
    
    frind_length = []
    for i in frind_li:
        frind_length.append(dijkstra(i))
    
    secret = inf
    for j in range(1, n+1):
        friendship = 0
        for i in range(frind):
            friendship += frind_length[i][j]
        if secret > friendship:
            secret = friendship
            result = j
    
    print(result)
            

            


