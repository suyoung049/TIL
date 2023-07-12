import sys

sys.stdin = open("31_직사각형합_input.txt", "r")

matrix = []
for _ in range(100):
    line = [0] * 100
    matrix.append(line)
for i in range(4):
    x_1, y_1, x_2, y_2 = map(int, input().split())
    for i in range(x_1, x_2):
        for j in range(y_1, y_2):
            matrix[i][j] = 1

sum_ = 0
for i in range(100):
    for j in range(100):
        if matrix[i][j] == 1:
            sum_ += 1
print(sum_)