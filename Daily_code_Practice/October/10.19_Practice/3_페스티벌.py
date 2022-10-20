import sys
from collections import deque
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    hy, hx = map(int, input().split())
    conv = [list(map(int, input().split())) for _ in range(n)]
    fy, fx = map(int, input().split())
    check = [False] * n


    def bfs(y, x):
        q = deque([(y,x)])

        while q:
            y, x = q.popleft()

            if abs(y-fy) + abs(x-fx) <= 1000:

                return 1

            for i in range(n):
                if not check[i]:
                    ny, nx = conv[i]
                    if abs(y-ny) + abs(x-nx) <= 1000:
                        q.append((ny,nx))
                        check[i] = True
    
    
    result = bfs(hy, hx)

    if result:
        print('happy')
    else:
        print('sad')
