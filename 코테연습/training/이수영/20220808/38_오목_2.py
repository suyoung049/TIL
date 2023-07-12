import sys

sys.stdin = open("38_input.txt", "r")

matrix = [list(map(int, input().split())) for _ in range(19)]

dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

black = 1
white = 2
answer = 0

for i in range(19):
    for j in range(19):
        if matrix[i][j] == 1 or matrix[i][j] == 2:
        
            for d in range(4):
                stone_count = 1
                ni = i + dx[d]
                nj = j + dy[d]

                while True:
                    if not(-1 < ni < 19 and -1 < nj < 19):
                        break
                    if (matrix[i][j] != matrix[ni][nj]):
                        break

                    stone_count += 1

                    ni = ni + dx[d]
                    nj = nj + dy[d]

                    if stone_count == 5:
                        prev_i = i - dx[d]
                        prev_j = j - dy[d]

                        if not(-1 < prev_i < 19 and -1 < prev_j < 19) or matrix[i][j] != matrix[prev_i][prev_j] :
                   
                            print(matrix[i][j])
                            print(i+1, j+1)

                            answer = matrix[i][j]


if answer == 0:
    print(answer)