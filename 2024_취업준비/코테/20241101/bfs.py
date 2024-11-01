import sys
from collections import deque
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline



node, edge, start = map(int, input().split())
graph = [[] for _ in range(node + 1)]
visit = [0] * (node + 1)
check = [False for _ in range(node + 1)]

# 그래프 생성
for _ in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 노드의 연결 리스트 정렬
for g in graph:
    g.sort()


queue = deque([(start)])
check[start] = True
cnt = 0

while queue:
    now = queue.popleft()
    cnt += 1
    visit[now] = cnt

    for n_node in graph[now]:
        if not check[n_node]:
            check[n_node] = True
            queue.append(n_node)

for i in range(1, node + 1):

    print(visit[i])
