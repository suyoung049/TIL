import sys
from collections import deque
sys.stdin = open('5_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
rev_graph = [[] for _ in range(n+1)]
depth = [0] * 10001
result = [0] * 10001
check = [False] * 10001

def topology_sort(q):

    while q:
        s_node = q.popleft()

        for n_node in graph[s_node]:
            if result[n_node[0]] <= n_node[1] + result[s_node]:
                result[n_node[0]] = n_node[1] + result[s_node]

            
            depth[n_node[0]] -= 1

            if depth[n_node[0]] == 0:
                q.append(n_node[0])
    
    count_ = 0
    q.append(end)
    check[end] = True

    while q:
        s_node = q.popleft()

        for n_node in rev_graph[s_node]:
            if result[s_node] - result[n_node[0]] == n_node[1]:
                count_ += 1

                if check[n_node[0]] == False:
                    q.append(n_node[0])
                    check[n_node[0]] = True
    
    return count_

for _ in range(m):
    y, x, time = map(int, input().split())

    graph[y].append((x,time))
    rev_graph[x].append((y,time))

    depth[x] += 1


start, end = map(int, input().split())


q = deque()
q.append(start)

node = topology_sort(q)

print(result[end])
print(node)


