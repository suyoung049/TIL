import sys

sys.stdin = open("2738_input.txt", "r")

def pprint(arr):
    for i in range(len(arr)):
        print(arr[i])

N, M = map(int, input().split())

matrix_1 = []
matrix_2 = []
matrix_sum = [[0] * M for _ in range(N)]

for _ in range(N):
    list_ = list(map(int, input().split()))
    matrix_1.append(list_)
for _ in range(N):
    list_2 = list(map(int, input().split()))
    matrix_2.append(list_2)
for i in range(N):
    for j in range(M):
        matrix_sum[i][j] = matrix_1[i][j] + matrix_2[i][j]
for i in range(N):
    print(*matrix_sum[i])