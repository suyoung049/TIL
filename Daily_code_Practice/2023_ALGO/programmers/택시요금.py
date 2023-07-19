# 전부 이어져 있어서 중간 경로를 시작점으로 변경해서 모든지점을 가는 비용의 최소값도 가능하다.
# 같이가야 한다는 점에 너무 집중하지 말자 모든 노드가 이어져 있어서 시작점을 지정하고 출발과 각각의 도착점의 최소값을 더하는것도 방법 

from heapq import heappop, heappush
n, s, a, b = 6, 4, 5, 6

fares = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]

inf = int(1e9)

graph = [[] for _ in range(n+1)]


def dijkstra(graph, k):
    heapque = []
    dijkstra_fare = [inf] * (n + 1)

    heappush(heapque, (k, 0))
    dijkstra_fare[k] = 0

    while heapque:
        y, cost = heappop(heapque)

        if dijkstra_fare[y] < cost:
            continue

        for taxi in graph[y]:
            sum_cost = taxi[1] + cost

            if dijkstra_fare[taxi[0]] > sum_cost:
                dijkstra_fare[taxi[0]] = sum_cost
                heappush(heapque, (taxi[0], sum_cost))
    
    return dijkstra_fare


for fare in fares:
    graph[fare[0]].append((fare[1], fare[2]))
    graph[fare[1]].append((fare[0], fare[2]))



answer = inf
for k in range(1, n+1):
    dijkstra_fare = dijkstra(graph, k)
    answer = min(answer, dijkstra_fare[s]+dijkstra_fare[a]+dijkstra_fare[b])

print(answer)
    