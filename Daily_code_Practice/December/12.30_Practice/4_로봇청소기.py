import sys
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

count = 0
n, m = map(int, input().split())
r, c, d = map(int, input().split())

matrix = list(list(map(int, input().split())) for _ in range(n))
visit = [[False] * m for _ in range(n)]

visit[r][c] = True
count = 1

while True:
    turn = 0

    for _ in range(4):
        ny = r + dy[(d+3)%4]
        nx = c + dx[(d+3)%4]

        d = (d+3)%4

        if 0<= ny < n and 0<= nx <m and matrix[ny][nx] == 0:
            if not visit[ny][nx]:
                visit[ny][nx] = True

                count += 1
                r = ny 
                c = nx

                turn = 1
                break

    if turn == 0:
        if matrix[r-dy[d]][c-dx[d]] == 1:
            print(count)
            break

        else:
            r, c = r-dy[d], c-dx[d] 
