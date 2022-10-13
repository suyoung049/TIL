import sys
sys.stdin = open('7_input.txt', 'r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

inf = sys.maxsize
n = int(input())

matrix = [[inf]*(n+1) for _ in range(n+1)]

m = int(input())

for _ in range(m):
    y, x, c = map(int, input().split())

    if matrix[y][x] > c:
        matrix[y][x] = c
for k in range(1, n+1):
    for j in range(1, n+1):
        for i in range(1, n+1):
            if j == i:
                matrix[j][i] = 0

            matrix[j][i] = min(matrix[j][i], matrix[j][k] + matrix[k][i])


for j in range(1, n+1):
    for i in range(1, n+1):
        if matrix[j][i] == inf: 
            print(0, end=' ')
        else:
            print(matrix[j][i], end=' ')
    print()

    