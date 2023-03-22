import sys
from collections import deque
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

def combine(q):

    while q:
        start = q.popleft()

        for next in graph[start]:
            for j in range(1, n+1):

                part[next[0]][j] += next[1] * part[start][j]
            
            deapth[next[0]] -= 1

            if deapth[next[0]] == 0:
                q.append(next[0])

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
part = [[0] * (n+1) for _ in range(n+1)]
deapth = [0] * (n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[y].append((x, z))
    deapth[x] += 1


q = deque()
for i in range(1, n+1):
    if deapth[i] == 0:
        part[i][i] = 1
        q.append(i)

combine(q)
pprint(part)


