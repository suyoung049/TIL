import sys
sys.stdin = open('2_input.txt', 'r')
from collections import deque
input = sys.stdin.readline

start, end = map(int, input().split())

move_check = [0] * 1000001

def bfs(start):
    q = deque([start])

    while q:
        y = q.popleft()

        if y == end:
            return

        for ny in (y+1, y-1, 2*y):
            if 0<= ny < 1000001 and move_check[ny] == 0:
                move_check[ny] = move_check[y] + 1
                q.append(ny)
bfs(start)

print(move_check[end])