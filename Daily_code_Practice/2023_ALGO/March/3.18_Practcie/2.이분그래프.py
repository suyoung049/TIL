import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

T = int(input())


def dfs(start, k):
    global bipartite
    check[start] = k

    if bipartite == False:
        return

    for j in graph[start]:
        if not check[j]:
            dfs(j, -k)
        
        elif check[start] == check[j]:
            bipartite = False
        

for _ in range(T):
    
    bipartite = True
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)] 
    check = [0] * (n+1)

    for _ in range(m):
        y, x = map(int, input().split())
        graph[y].append(x)
        graph[x].append(y)
    
    for i in range(1, n+1):
        if not check[i]:
            dfs(i, 1)

        if bipartite == False:
            break

    
    if bipartite == True:
        print('YES')
    
    else:
        print('NO')


