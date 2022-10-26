import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
m = int(input())


def pprint(list_):
    for row in list_:
        print(row)


matrix = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    y, x = map(int, input().split())

    matrix[y][x] = 1

for k in range(1, n+1):
    for j in range(1, n+1):
        for i in range(1, n+1):

            if matrix[j][k] == 1 and matrix[k][i] == 1:
                matrix[j][i] = 1

for j in range(1, n+1):
    answer = 0
    for i in range(1, n+1):
        answer += matrix[j][i] + matrix[i][j]
    print(n-answer-1)