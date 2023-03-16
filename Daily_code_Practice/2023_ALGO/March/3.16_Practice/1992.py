import sys
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

matrix = [list(input().strip()) for _ in range(n)]


def divide(y, x, n):
    for j in range(y, y+n):
        for i in range(x, x+n):
            if matrix[y][x] != matrix[j][i]:
                print('(', end='')
                divide(y, x, n//2)
                divide(y, x+n//2, n//2)
                divide(y+n//2, x, n//2)
                divide(y+n//2, x+n//2, n//2)
                print(')', end='')
                return


    if matrix[y][x] == '1':
        print('1', end='')

    else:
        print('0', end='')

divide(0, 0, n)