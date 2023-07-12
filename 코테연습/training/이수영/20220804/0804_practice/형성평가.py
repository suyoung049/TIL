import sys

sys.stdin = open("1_input.txt", "r")

matrix_1 = [list(map(int, input().split())) for _ in range(2)]
matrix_2 = [list(map(int, input().split())) for _ in range(2)]

list_ = [[0] * 3 for _ in range(2)]
for i in range(2):
    for j in range(3):
        list_[i][j] = matrix_1[i][j] * matrix_2[i][j]

for i in range(2):
    for j in range(3):
        print(list_[i][j], end = ' ')
    print()