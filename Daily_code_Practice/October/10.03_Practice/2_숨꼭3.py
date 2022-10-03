import sys
from collections import deque
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())

stay = [-1] * 101

def bfs(n):
    stay[n] = 0

    q = deque([n])

    while q:
        y = q.popleft()

        if y == m:
            return

        for ny in (y+1, y-1, 2*y):
            if 0<= ny < 101 and stay[ny] == -1:
                if ny == 2*y:
                    stay[ny] = stay[y]
                    q.appendleft(ny)

                if ny == y+1 or ny == y-1:
                    stay[ny] = stay[y] +1
                    q.append(ny)

bfs(n)
print(stay[m])