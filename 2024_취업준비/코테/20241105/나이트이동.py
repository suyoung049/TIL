import sys
sys.stdin = open('1_input.txt', 'r')
from collections import deque
input = sys.stdin.readline

def pprint(matrix):
    for x in matrix:
        print(x)

dy = [-1, -2, 1, 2, 2, 1, -1, -2]
dx = [-2, -1, -2, -1, 1, 2, 2, 1]

test_n = int(input())

for _ in range(test_n):
    m = int(input())
    check = [[False for _ in range(m)] for _ in range(m)]
    s_y, s_x = map(int, input().split())
    e_y, e_x = map(int, input().split())

    queue = deque([(s_y, s_x, 0)])
    check[s_y][s_x] = True
    answer = 0
    while queue:
        y, x, cnt = queue.popleft()

        if y == e_y and x == e_x:
            answer = cnt
            break

        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < m and 0<= nx < m and not check[ny][nx]:
                check[ny][nx] = True
                queue.append((ny, nx, cnt+1))

    print(answer)
    

    