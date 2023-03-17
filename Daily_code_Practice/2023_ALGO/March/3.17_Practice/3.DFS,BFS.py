import sys
from collections import deque
sys.stdin = open('3_input.txt','r')
sys.setrecursionlimit(10**6)

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]


for _ in range(m):
    y, x = map(int, input().split())
    graph[y].append(x)
    graph[x].append(y)


for i in graph:
    i.sort()

def dfs(start, graph, check):
    check[start] = True
    print(start, end=' ')

    for i in graph[start]:
        if not check[i]:
            dfs(i, graph, check)

def bfs(start, graph, check):
    check[start] = True
    q = deque([start])

    while q:
        j = q.popleft()
        print(j, end=' ')

        for i in graph[j]:
            if not check[i]:
                check[i] = True
                q.append(i)


check = [False] * (n+1)
dfs(v, graph, check)

print()

check = [False] * (n+1)
bfs(v, graph, check)