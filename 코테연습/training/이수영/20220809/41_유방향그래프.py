import sys

sys.stdin = open("40_input.txt", "r")

N, M = map(int, input().split())

graph = [[0] * (N+1) for _ in range(N+1)]
graph_list = [[] for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph_list[v1].append(v2)
    graph[v1][v2] = 1
print(graph)
print(graph_list)

