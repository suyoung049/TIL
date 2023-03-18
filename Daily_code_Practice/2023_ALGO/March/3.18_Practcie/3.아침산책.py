import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

inside = [0] + list(map(int, input().strip()))
graph = [[] for _ in range(n+1)]


for _ in range(n-1):
    y, x = map(int, input().split())

    graph[y].append(x)
    graph[x].append(y)


def dfs(start, graph, check, state):
    check[start] = True
    if state == False:
        return

    for j in graph[start]:
        if inside[j] == 0 and not check[j]:
            dfs(j, graph, check, state)
        
        elif inside[j] == 1 and not check[j]:
            state = False
            dfs(j, graph, check, state)

root_sum = 0

state = True
for i in range(1, n+1):
    root = -1
    if inside[i] == 0:
        continue
    else:
        check = [False] * (n+1)

        dfs(i, graph, check, state)

    for j in range(1, n+1):
        
        if inside[j] == 1 and check[j]:
            root += 1
    
    root_sum += root

print(root_sum)
