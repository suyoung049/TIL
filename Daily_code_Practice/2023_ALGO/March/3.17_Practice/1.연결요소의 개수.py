import sys
sys.stdin = open('1_input.txt','r')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
check = [False] * (n+1)

for _ in range(m):
    y, x = map(int, input().split())
    graph[y].append(x)
    graph[x].append(y)

def dfs(i, graph, check):
    check[i] = True

    for j in graph[i]:
        if not check[j]:
            dfs(j, graph, check)


count_ = 0
for i in range(1, n+1):
    if not check[i]:
        count_ += 1
        dfs(i, graph, check)
print(count_)