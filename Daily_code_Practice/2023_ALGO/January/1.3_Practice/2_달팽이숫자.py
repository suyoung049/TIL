import sys
sys.stdin = open("2_input.txt", 'r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

T = int(input())

for test_case in range(1, T+1):
    n = int(input())

    matrix = [[0] *n for _ in range(n)]
    
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    y, x = 0, 0
    len_ = 0

    for i in range(1, (n*n)+1):
        matrix[y][x] = i

        ny = y + dy[len_]
        nx = x + dx[len_]

        if not(0<= ny < n and 0 <= nx < n) or matrix[ny][nx] != 0:
                ny = y - dy[len_]
                nx = x - dx[len_]

                len_ = (1+len_)%4

                ny = y+ dy[len_]
                nx = x + dx[len_]

        y = ny
        x = nx 
    print(f'#{test_case}')
    for j in range(n):
        for i in range(n):
            print(matrix[j][i], end = ' ')
        print()

