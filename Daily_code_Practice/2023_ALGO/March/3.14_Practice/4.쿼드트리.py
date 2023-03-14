import sys
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

n = int(input())

matrix = [list(input().strip()) for _ in range(n)]


answer = ''
def divide(y, x, n):
    global answer
    for j in range(y, y + n):
        for i in range(x, x + n):
            if matrix[y][x] != matrix[j][i]:
                print('(', end='')
                divide(y, x, n//2)
                divide(y, x+n//2, n//2)
                divide(y+n//2, x, n//2)
                divide(y+n//2, x+n//2, n//2)
                print(')', end='')
                return

    
    
    if matrix[y][x] == '1':
        answer += '1'
        print('1', end='')
    
    else:
        answer += '0'
        print('0', end='')


divide(0, 0, n)
