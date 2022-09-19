import sys
from collections import deque

sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

N, M, K = map(int, input().split())

graph_list = [[] for _ in range(N+1)]

visited = [False] * (N+1)

for _ in range(M):
    v1, v2 = map(int,input().split())
    graph_list[v1].append(v2)
    graph_list[v2].append(v1)

for i in range(len(graph_list)):
    graph_list[i].sort()

def dfs(start):
    
    visited[start] = True
    print(start, end =' ')
    for i in graph_list[start]:
        if not visited[i]:
            dfs(i)
            


def bfs(start):
    q=deque([start])
    visited[start]=True
    while q:
        now=q.popleft()
        print(now,end=' ')
        for i in graph_list[now]:
            if not visited[i]:
                visited[i]=True
                q.append(i)
                
dfs(K)
visited=[False]*(N+1)
print()
bfs(K)


