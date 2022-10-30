import sys
sys.stdin = open('2_input.txt', 'r')
from collections import deque
input = sys.stdin.readline

n, m, s = map(int, input().split())

matrix = [[] for _ in range(n+1)]
rev_matrix = [[] for _ in range(n+1)]

for _ in range(m):
    y, x = map(int, input().split())

    matrix[y].append(x)
    rev_matrix[x].append(y)
print(matrix)
print(rev_matrix)
visited = [False] * (n+1)

def bfs_1(start):
    cnt_1 = 0
    q = deque([start])
    visited[start] = True


    while q:
        y = q.popleft()

        for i in matrix[y]:
            if not visited[i]:
                visited[i] = True
                cnt_1 += 1
                q.append(i)
    
    return cnt_1

visited = [False] * (n+1)

def bfs_2(start):
    cnt_2 = 0
    q = deque([start])
    visited[start] = True

    while q:
        y = q.popleft()
        for i in rev_matrix[y]:
            if not visited[i]:
                visited[i] = True
                cnt_2 += 1
                q.append(i)

    return cnt_2

good = bfs_1(s)
bad = bfs_2(s)

print(bad+1, n-good)



    




