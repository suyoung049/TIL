import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline
from heapq import heappop, heappush


def short_root(start, end, graph, dp, limit):
    answer = False
    heap = []
    dp[start] = 0
    heappush(heap, (0, start))

    while heap:
        time, node = heappop(heap)
        for next_node, t in graph[node]:
            next_time = time + t
            if dp[next_node] > next_time:
                dp[next_node] = next_time
                heappush(heap, (next_time, next_node))
    
    if dp[end] < limit:
        answer = True
    
    return answer

n = int(input())

for _ in range(n):
    result = 'YES'
    INF = 1000000
    node, root, wormhole = map(int, input().split())
    graph = [[] for _ in range(node + 1)]
    for _ in range(root):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    wormhole_list = []
    for _ in range(wormhole):
        start, end, time = map(int, input().split())
        wormhole_list.append((start, end, time))

    for start, end, time in wormhole_list:
        dp = [INF for _ in range(node + 1)]
        answer = short_root(start, end, graph, dp, time)
        
        if answer == False:
            result = "NO"
            break

    print(result)