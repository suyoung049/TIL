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
    n = int(input())

    sy, sx = map(int, input().split())
    ey, ex = map(int, input().split())

    matrix = [[-1] * n for _ in range(n)]

    def bfs(y,x):
        q = deque([(y,x)])
        

        matrix[y][x] = 0

        while q:
            (y,x) = q.popleft()

            if (y,x) == (ey, ex):
                
                return matrix[y][x]


            for i in range(8):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0 <= ny < n and 0 <= nx < n:
                    if matrix[ny][nx] == -1:
                        matrix[ny][nx] = matrix[y][x] + 1
                        q.append((ny,nx))
    
    print(bfs(sy,sx))
    

