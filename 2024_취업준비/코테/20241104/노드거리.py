import sys
sys.stdin = open('1_input.txt', 'r')
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(start, target, check_list, graph):
    if start == target:
        return 0
    
    check_list[start] = True
    
    for next_node,cost in graph[start]:
        if not check_list[next_node]:
            result = dfs(next_node, target, check_list, graph)
            if result != -1:
                return result + cost
    
    return -1



n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))


for _ in range(m):
    start, target = map(int, input().split())
    check_li = [False for _ in range(n+1)]
    result = dfs(start, target, check_li, graph)
    print(result)