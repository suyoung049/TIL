import sys
from collections import deque
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
check = [-1 for _ in range(n+1)]  # 초기값 -1로 설정해 미방문 노드 표시
answer = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

queue = deque([x])
check[x] = 0  # 시작 노드의 거리를 0으로 설정

while queue:
    node = queue.popleft()

    for n_node in graph[node]:
        if check[n_node] == -1:  # 미방문 노드만 처리
            check[n_node] = check[node] + 1
            queue.append(n_node)
            
result = False

for i in range(1, n+1):
    if check[i] == k:
        result = True
        print(i)

if not result:
    print(-1)