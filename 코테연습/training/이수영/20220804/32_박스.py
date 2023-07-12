import sys

sys.stdin = open("32_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    print(matrix)
    box = []
    for j in range(M):
        box_line = [matrix[i][j] for i in range(N)]
        box.append(box_line)
    print(box)
    move = 0
    for j in range(M):
        for i in range(N):
            if box[j][i] == 1:
                for x in range(i+1, N):
                    if box[j][x] == 0:
                        move += 1
    print(move)