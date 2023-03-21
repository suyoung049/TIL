import sys
sys.stdin = open('4_input.txt', 'r')
from collections import deque
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

def combin(q):

    while q:
        start = q.popleft()

        for next in graph[start]:
            for i in range(n+1):
                part[next[0]][i] += next[1] * part[start][i]
            depth[next[0]] -= 1

            if depth[next[0]] == 0:
                q.append(next[0])

n = int(input())
m = int(input())


graph = [[] for _ in range(n+1)]
depth = [0] * (n+1)
part = [[0] * (n+1) for _ in range(n+1)]


for _ in range(m):
    x, y, z = map(int, input().split())
    graph[y].append((x,z))

    depth[x] += 1


q = deque()
for i in range(1, n+1):
    if depth[i] == 0:
        q.append(i)
        part[i][i] = 1

combin(q)


for i in range(1,n+1):
    if part[n][i]:
        print(f'{i} {part[n][i]}')


