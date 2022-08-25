import sys
sys.stdin = open('1_input.txt', 'r')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    matrix = [[0]*n for _ in range(n)]

    r, c = 0, 0
    dist = 0

    for i in range(1, n*n + 1):
        matrix[r][c] = i
        r += dr[dist]
        c += dc[dist]

        if r < 0 or c < 0 or r >= n or c >= n or matrix[r][c] != 0:
            r -= dr[dist]
            c -= dc[dist]

            dist = (dist+1) % 4

            r += dr[dist]
            c += dc[dist]
    print(f'#{test_case}')
    for row in matrix:
        print(*row)
    print()