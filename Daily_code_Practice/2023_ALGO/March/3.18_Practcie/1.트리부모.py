import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
m = n-1

graph = [[] for _ in range(n+1)]
check = [False] * (n+1)

for _ in range(m):
    y, x = map(int, input().split())

    graph[y].append(x)
    graph[x].append(y)

def dfs(start, back, graph, check):
    check[start] = back

    for i in graph[start]:
        if not check[i]:
            dfs(i, start, graph, check)
    
dfs(1, 0, graph, check)
for i in range(2, n+1):
    print(check[i])