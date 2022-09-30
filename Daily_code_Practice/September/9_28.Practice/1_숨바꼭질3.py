import sys
from collections import deque
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())

stay = [-1] * 100001

def bfs(start):
    q = deque([start])
    stay[start] = 0

    while q:
        y = q.popleft()

        if y == m:
            return stay[y]

        for ny in (y+1, y-1, y*2):
            if 0 <= ny < 100001 and stay[ny] == -1:
                if ny == y*2:
                    stay[ny] = stay[y]
                    q.appendleft(ny)

                else:
                    stay[ny] = stay[y] + 1
                    q.append(ny)

print(bfs(n))

