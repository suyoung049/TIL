import sys
from collections import deque
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
check = [False] * (n+1)

for _ in range(m):
    y, x = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(start, graph, check):
    check[start] = True
    q = deque([start])

    while q:
        j = q.popleft()

        for i in graph[j]:
            if not check[i]:
                check[i] = True
                q.append(i)

bfs(1, graph, check)

count_ = 0
for i in range(2,n+1):
    if check[i] == True:
        count_ += 1

print(count_)