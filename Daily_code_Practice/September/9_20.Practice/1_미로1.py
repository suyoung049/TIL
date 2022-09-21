import sys
from collections import deque
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def pprint(list_):
    for row in list_:
        print(row)


matrix = [list(map(int, input().strip())) for _ in range(16)]
check = [[0] * 16 for _  in range(16)]
home = 'False'

def bfs(y,x):
    global home
    q = deque([(y,x)])
    check[y][x] = 1

    while q:
        y,x = q.popleft()

        if matrix[y][x] == 3:
            home = 'succes'

        for i in range(4):

            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < 16 and 0<= nx < 16 and check[ny][nx] == 0:
                if matrix[ny][nx] == 3 or matrix[ny][nx] == 0:
                    check[ny][nx] = 1
                    q.append((ny,nx))

bfs(1,1)
pprint(check)
if home == 'succes':
    print(1)
else:
    print(0)


            


