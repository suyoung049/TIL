import sys
sys.stdin = open('3_input.txt')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)
n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):    # 거쳐가는 중간경로의 범위를 가장 앞에 둔다. (플로이드 와샬)
    for j in range(n):
        for i in range(n):
            if matrix[i][k] == 1 and matrix[k][j] == 1:
                matrix[i][j] = 1

for row in matrix:
    print(*row)