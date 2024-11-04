import sys
sys.setrecursionlimit(10 ** 6)
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

def dfs(start, end, check_li, graph):
    if start == end:
        return 0
    
    check_li[start] = True
    
    for n_node in graph[start]:
        if not check_li[n_node]:
            result = dfs(n_node, end, check_li, graph)
            if result != -1:
                return result + 1
    
    return -1


n = int(input())

start, end = map(int, input().split())

graph = [[] for _ in range(n+1)]

m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

    check_list = [False for _ in range(n+1)]

print(dfs(start, end, check_list, graph))

