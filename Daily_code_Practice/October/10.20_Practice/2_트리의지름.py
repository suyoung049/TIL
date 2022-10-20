import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline



def dfs(y, x):

    for v, d in matrix[y]:
        if visit[v] == -1:
            visit[v] = x + d
            dfs(v, x+d)
    
n = int(input())

matrix = [[] for _ in range(n+1)]

for _ in range(n-1):
    y, x, k = map(int, input().split())

    matrix[y].append((x, k))
    matrix[x].append((y, k))

visit = [-1] * (n+1)

visit[1] = 0
dfs(1, 0)
k = visit.index(max(visit))

visit = [-1] * (n+1)

visit[k] = 0
dfs(k,0)

print(max(visit))


            



