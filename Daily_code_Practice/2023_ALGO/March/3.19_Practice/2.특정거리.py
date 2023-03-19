import sys
from collections import deque
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

n, m, k, rode = map(int, input().split())


graph = [[] for _ in range(n+1)]
check = [False] * (n+1) 

for _ in range(m):
    y, x = map(int, input().split())
    graph[y].append(x)


result = []
def bfs(start, short):

    use = True
    q = deque([(start, short)])
    check[start] = True

    while q:
        y, short = q.popleft()

        if short == k:
            print(y)
          

        for j in graph[y]:
            if not check[j]:
                check[j] = True
                q.append((j, short+1))
    
bfs(rode, 0)
if not result:
    print(-1)

else:
    result.sort()

    for i in result:
        print(i)





