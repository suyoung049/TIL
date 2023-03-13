import sys
sys.stdin = open('5_input.txt', 'r')
input = sys.stdin.readline


N, M = map(int, input().split())
matrix_a = [list(map(int, input().split())) for _ in range(N)]
print(matrix_a)

M, N = map(int, input().split())
matix_b = [list(map(int, input().split())) for _ in range(M)]
print(matix_b)

matix_c = list([0] * N for _ in range(N))

for j in range(N):
    for k in range(N):
        for i in range(M):
            matix_c[j][k] += matrix_a[j][i] * matix_b[i][k]

for i in matix_c:
    for j in i:
        print(j, end=' ')
    print()