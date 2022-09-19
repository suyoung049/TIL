import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

n, m, k = map(int, input().split())

matrix = [[] for _ in range(n+1)]
check = [False] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    matrix[x].append(y)
    matrix[y].append(x)

for i in range(len(matrix)):
    matrix[i].sort()

def dfs(start):
    check[start] = True
    print(start, end = ' ')

    for i in matrix[start]:
        if check[i] == False:
            check[i] = True
            dfs(i)

def bfs(now):
    check[now] = True
    q = deque([now])

    while q:
        j = q.popleft()
        print(j, end = ' ')

        for i in matrix[j]:
            if check[i] == False:
                check[i] = True
                q.append(i)


dfs(k)
check = [False] * (n+1)
print()
bfs(k)

