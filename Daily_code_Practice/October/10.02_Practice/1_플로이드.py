import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

inf = sys.maxsize

n = int(input())

matrix = [[inf] * n for _ in range(n)]

m = int(input())

for _ in range(m):
    j , i , k = map(int, input().split())

    if k < matrix[j-1][i-1]:
        matrix[j-1][i-1] = k

for k in range(n):
    for y in range(n):
        for x in range(n):
            matrix[y][x] = min(matrix[y][x], matrix[y][k] + matrix[k][x])
            
            if y == x:
                matrix[y][x] = 0

for j in range(n):
    for i in range(n):
        if matrix[j][i] == inf:
            print(0, end = ' ')
        else:
            print(matrix[j][i], end = ' ')

    print()


