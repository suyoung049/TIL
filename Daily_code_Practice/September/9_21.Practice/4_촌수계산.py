import sys
sys.stdin = open('4_input.txt', 'r')
from collections import deque
input = sys.stdin.readline

n = int(input())
h, k = map(int, input().split())
m = int(input())

matrix = [[] for _ in range(n+1)]
check = [-1] * (n+1)


for _ in range(m):
    y, x = map(int, input().split())

    matrix[y].append(x)
    matrix[x].append(y)

def bfs(y):
    q = deque([y])
    check[y] = 0

    while q:
        y = q.popleft()

        for i in matrix[y]:
            if check[i] == -1:
                check[i] = check[y] + 1
                q.append(i)

bfs(k)
if check[h] != 0:
    print(check[h])
else:
    print(-1)
