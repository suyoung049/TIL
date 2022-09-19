import sys
from collections import deque
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

n,m,k = map(int, input().split())

matrix = [[] for _ in range(n+1)]
check = [0] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    matrix[x].append(y)
    matrix[y].append(x)


for i in range(len(matrix)):
    matrix[i].sort()


def bfs(start):
    count = 1
    q = deque([start])
    check[start] = count

    while q:
        now = q.popleft()
       

        for i in matrix[now]:
            if check[i] == 0:
                count += 1
                check[i] = count
                q.append(i)

bfs(k)
for i in range(1,n+1):
    print(check[i])
