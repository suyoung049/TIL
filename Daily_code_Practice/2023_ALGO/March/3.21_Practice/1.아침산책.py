import sys
sys.stdin = open('1_input.txt', 'r')
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())

rode_type = [0] + list(map(int, input().strip()))

answer = 0

graph = [[] for _ in range(n+1)]
check = [False] * (n+1)

for _ in range(n-1):
    y, x = map(int, input().split())
    graph[y].append(x)
    graph[x].append(y)

    if rode_type[y] == 1 and rode_type[x] == 1:
        answer += 2

def dfs(outside, graph, check, inside_count):
    check[outside]  = True

    for j in graph[outside]:
        if rode_type[j] == 1:
            inside_count += 1

        elif rode_type[j] == 0 and not check[j]:
             inside_count = dfs(j, graph, check, inside_count)
    
    return inside_count

for i in range(1, n+1):
    inside_count = 0
    if rode_type[i] == 0 and not check[i]:
        x = dfs(i, graph, check, inside_count)
        answer += x * (x-1)


print(answer)




