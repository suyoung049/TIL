import sys
from collections import deque
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

dy = [1, 1, -1, -1, 2, 2, -2, -2]
dx = [2, -2, -2, 2, 1, -1, 1, -1]

T = int(input())

for _ in range(T):
    m = int(input())
    sy, sx = map(int, input().split())
    fy, fx = map(int, input().split())

    check = [[0]*m for _ in range(m)]

    def bfs(y,x):

        q = deque([(y, x)])

        while q:
            y, x = q.popleft()

            if (y, x) == (fy,fx):
                return check[y][x]
                
            for i in range(8):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0 <= ny < m and 0 <= nx <m and not check[ny][nx]:
                    check[ny][nx] = check[y][x] + 1
                    q.append((ny,nx))

    print(bfs(sy,sx))
    