import sys
from collections import deque
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline


n, m = map(int, input().split())

matrix = [[] for _ in range(n+1)]



for _ in range(n-1):
    y, x, k = map(int, input().split())

    matrix[y].append((x,k))
    matrix[x].append((y,k))



def bfs(start, end):
    check = [False] * (n+1)

    q = deque([(start,0)])
    check[start] = True

    while q :
        v, d = q.popleft()

        if v == end:
            return d

        for i,k in matrix[v]:
            if not check[i]:
                check[i] = True
                q.append((i, k+d))
    

for _ in range(m):
    y, x = map(int, input().split())
    print(bfs(y, x))

