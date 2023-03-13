import sys
sys.stdin = open('7_input.txt', 'r')
input = sys.stdin.readline


n, b = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]


def fastpower(n, matrix_1, matrix_2):
    result = list([0] * n for _ in range(n))

    for j in range(n):
        for k in range(n):
            for i in range(n):
                result[j][k] += matrix_1[j][i] * matrix_2[i][k]
            
            result[j][k] %= 1000
    
    return result


def divide(n, b, matrix):
    if b == 1:
        return matrix
    
    if b == 2:
        return fastpower(n, matrix, matrix)

    temp = divide(n, b//2, matrix)
    if b % 2 == 0:
        return fastpower(n, temp, temp)

    else:
        return fastpower(n, fastpower(n, temp, temp), matrix)


result = divide(n,b,matrix)

for row in result:
    for num in row:
        print(num % 1000, end=' ')
    print()