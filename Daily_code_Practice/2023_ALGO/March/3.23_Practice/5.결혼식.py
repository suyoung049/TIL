import sys
from collections import deque
sys.stdin = open('5_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
check = [False] * (n+1)

for _ in range(m):
    y, x = map(int, input().split())
    graph[y].append(x)
    graph[x].append(y)


def bfs(start):
    check[start] = True
    q = deque([start])

    count_ = 0
    depth = 0
    while q:

        if depth == 2:
            break
    
        for _ in range(len(q)):
            
            y = q.popleft()

            for j in graph[y]:
                if not check[j]:
                    check[j] = True
                    count_ += 1
                    q.append(j)
        depth += 1
    
    return count_
        
print(bfs(1))