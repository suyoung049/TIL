import sys
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline
def pprint(list_):
    for row in list_:
        print(row)

n, m = map(int, input().split())

matrix = [[0] *(n+1) for _ in range(n+1)]

for _ in range(m):
    j, i = map(int, input().split())
    matrix[j][i] = 1
    matrix[i][j] = 1
for k in range(1, n+1):
    for j in range(1, n+1):
        for i in range(1, n+1):
            if i == j:
                continue
            elif matrix[i][k] and matrix[k][j]:
                if matrix[i][j] == 0:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
                else:
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j] )
                

result = sys.maxsize

for i in range(1, n+1):
    sum_ = 0
    for j in range(1, n+1):
        sum_ += matrix[i][j]
    if result > sum_:
        result = sum_
        p = i
print(p)
       