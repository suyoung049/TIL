import sys

sys.stdin = open("44_input.txt", "r")

N, M = map(int, input().split())

graph_list = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    v1, v2 = map(int, input().split())

    graph_list[v1].append(v2)
    graph_list[v2].append(v1)

def dfs(start):
    stack = [start]
    visited[start] = True

    while stack:
        current = stack.pop()

        for adj in graph_list[current]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)
coun = 0
for j in range(1, N+1):
    if not visited[j]:
        dfs(j)
        coun += 1
print(coun)







