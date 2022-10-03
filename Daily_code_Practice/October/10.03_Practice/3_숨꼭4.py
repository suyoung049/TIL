import sys
from collections import deque
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())

stay = [-1] * 101
visit = [0] * 101

def move(m):
    result = [m]
    temp = visit[m]
    for _ in range(stay[m]):
        result.append(temp)
        temp = visit[temp]
    print(' '.join(map(str, result[::-1])))




def bfs(n):
    stay[n] = 0

    q = deque([n])

    while q:

        y = q.popleft()

        if y == m:
            move(m)
            return

        
        for ny in (y+1, y-1, 2*y):
            if 0 <= ny < 101:
                if stay[ny] == -1 or stay[ny] >= stay[y] + 1:
                    stay[ny] = stay[y] + 1
                    visit[ny] = y
                    q.append(ny)

bfs(n)