import sys
sys.stdin = open("1_input.txt", "r")
from collections import deque

input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

monkey_y = [0, 1, 0, -1]
monkey_x = [1, 0, -1, 0]

horse_y = [2, 2, -2, -2, 1, 1, -1, -1]
horse_x = [1, -1, 1, -1, 2, -2, 2, -2]


k = int(input())

m, n = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
check = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]


def bfs(cnt, y, x):
    q = deque([(cnt, y, x)])
    check[y][x][cnt] = 1

    while q:
        y, x, cnt = q.popleft()

        if (y, x) == (n-1, m -1):
            return check[y][x][cnt] -1 

        for i in range(4):
            ny = y + monkey_y[i]
            nx = x + monkey_x[i]

            if 0 <= ny < n and 0<= nx < m and not check[ny][nx][cnt]:
                if matrix[ny][nx] != 1:
                    check[ny][nx][cnt] = check[y][x][cnt] + 1
                    q.append((ny, nx, cnt))
        
        if cnt < k:
            for i in range(8):
                ny = y + horse_y[i]
                nx = x + horse_x[i]

                if 0<= ny < n and 0<= nx < m and not check[ny][nx][cnt+1]:
                    if matrix[ny][nx] != 1:
                        check[ny][nx][cnt+1] = check[y][x][cnt] + 1
                        q.append((ny, nx, cnt+1))
        
        
    return -1
        
print(bfs(0, 0, 0))
pprint(check)