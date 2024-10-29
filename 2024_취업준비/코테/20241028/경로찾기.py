import sys
sys.stdin = open('1_input.txt', 'r')

def pprint(matrix):
    for x in matrix:
        print(list(x))


n = int(input())

# 0 1 0
# 0 0 1
# 1 0 0
matrix = [list(map(int, input().split()))  for _ in range(n)]

# 플로이드 워셜
for k in range(n):
    for j in range(n):
        for i in range(n):
            if matrix[j][i] == 0:
                # 점화식 규칙
                if matrix[j][k] == 1 and matrix[k][i] == 1:
                    matrix[j][i] = 1

# 플로이드 워셜
for k in range(n):
    for j in range(n):
        for i in range(n):
            if matrix[j][i] == 0:
                # 점화식 규칙
                matrix[j][i] = min(matrix[j][i], matrix[j][k] + matrix[k][i])
                    
pprint(matrix)
