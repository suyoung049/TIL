import sys
from collections import deque
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
m = int(input())

graph_list = [[] for _ in range(n+1)]
visit = [False] * (n+1)

for _ in range(m):
    y,x = map(int, input().split())

    graph_list[y].append(x)
    graph_list[x].append(y)

def bfs(x):
    count = 1
    q = deque([x])
    visit[x] = True

    while q:
        now = q.popleft()

        for num_ in graph_list[now]:
            if visit[num_] == False:
                visit[num_] = True
                q.append(num_)
                count +=1
    
    return count-1     

print(bfs(1))       





