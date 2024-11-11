import sys
sys.stdin = open('2_input.txt', 'r')
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(graph, start, check):
    global yes_li
    global result
    if not graph[start]:
        if not check:
            result = False 
        return
    
    for n_node in graph[start]:
        if n_node in yes_li:
            dfs(graph, n_node, True)
        else:
            dfs(graph, n_node, check)
    

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

k = int(input())

yes_li = list(map(int, input().split()))
result = True
start = 1
if start in yes_li:
    print("Yes")
else:
    dfs(graph, start, False)
    if not result:
        print("yes")
    else:
        print("Yes")
    


