import sys
from collections import deque
sys.stdin = open("43_input.txt", "r") 

N = int(input())
M = int(input())

graph_list = [[] for _ in range(N+1)]
visited = [False] * (N+1)


for _ in range(M):
    v1, v2 = map(int, input().split())
    graph_list[v1].append(v2)
    graph_list[v2].append(v1)

def dfs(start):
    stack = deque([start])
    visited[start] = True

    while stack:
        current = stack.popleft()

        for adj in graph_list[current]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)
dfs(1)
print(visited)
print(visited.count(True) - 1)
