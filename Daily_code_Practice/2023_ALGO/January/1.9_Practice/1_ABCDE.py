import sys
sys.stdin = open('1_input.txt', 'r')
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


n, m = map(int, input().split())

graph = [[] for _ in range(n)]
check = [False for _ in range(n)]

result = False

for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)


def dfs(i, s):
    global result
   

    if s == 4:
        result = True
        return 

    
    for y in graph[i]:
        if not check[y]:
            check[y] = True 
            n = s + 1
            dfs(y, n)
    
    check[i] = False

for i in range(n):
    check[i] = True
    dfs(i, 0)
    if result:
        break


if result:
    print(1)

else:
    print(0)
