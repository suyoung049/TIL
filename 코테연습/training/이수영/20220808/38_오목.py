import sys

sys.stdin = open("38_input.txt", "r")

matrix = [list(map(int, input().split())) for _ in range(19)]

dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for i in range(19):
    for j in range(19):
        if matrix[i][j] != 0:
            stone = matrix[i][j]

            for d in range(4):
                coun = 1
                s_i = i + dx[d]
                s_j = j + dy[d]

                while 0 <= s_i < 19 and 0 <= s_j < 19 and matrix[s_i][s_j] == stone:
                    coun += 1

                    if coun == 5:
                        if 0 <= i - dx[d] < 19 and 0 <= j - dy[d] < 19 and matrix[i - dx[d]][j - dy[d]] == stone:
                            break
                        if 0 <= s_i + dx[d] < 19 and 0<= s_j + dy[d] and matrix[s_i + dx[d]][s_j + dy[d]] == stone:
                            break
                        print(stone)
                        print(i+1, j+1)
                        sys.exit(0)
                    s_i += dx[d]
                    s_j += dy[d]
print(0)
                       


            

