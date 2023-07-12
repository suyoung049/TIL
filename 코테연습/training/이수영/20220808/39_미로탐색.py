import sys

sys.stdin = open("39_input.txt", "r")
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
N, M = map(int, input().split())
matrix = [list(input()) for _ in range(N)]
coun = 0

for i in range(N):
    for j in range(M):
        for d in range(4):
            move_i = i + dx[d]
            move_j = j + dx[d]

            if 0 <= move_i <= N-1 and 0 <= move_j <= M-1:
                if matrix[move_i][move_j] == '1':
                    coun += 1
                    matrix[i][j] = matrix[move_i][move_j]
