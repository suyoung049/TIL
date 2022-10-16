import sys
sys.stdin = open('8_input.txt','r')
from collections import deque
input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())

stair = [-1] * (f+1)


q = deque([s])

while q:
    stair[s] = 0

    y = q.popleft()

    for ny in (y+u, y-d):
        if 0 < ny < f+1:
            if stair[ny] == -1:
                stair[ny] = stair[y] + 1
                q.append(ny)


if stair[g] == -1:
    print('use the stairs')
else:
    print(stair[g])