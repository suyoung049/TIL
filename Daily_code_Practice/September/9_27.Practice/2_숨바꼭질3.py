import sys
sys.stdin = open('2_input.txt', 'r')
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

q = deque()
q.append(n)

visited = [-1] * 100001
visited[n] = 0

while q:
    y = q.popleft()
    if y == m:
        print(visited[y])
        break

    if 0<= y -1 < 100001 and visited[y-1] == -1:
        visited[y-1] = visited[y] + 1
        q.append(y-1)

    if 0 <= y*2 < 100001 and visited[y*2] == -1:
        visited[y*2] = visited[y]
        q.appendleft(y*2)

    if 0<= y+1 < 100001 and visited[y+1] == -1:
        visited[y+1] = visited[y] + 1
        q.append(y+1)