import sys
sys.stdin = open('6_input.txt', 'r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

n = int(input())

matrix = [list(map(int, input().strip())) for _ in range(n)]
pprint(matrix)

def quad(y,x,n):

    for j in range(y,y+n):
        for i in range(x,x+n):
            if matrix[y][x] != matrix[j][i]:
                print('(', end = '')
                quad(y,x,n//2)
                quad(y,x+n//2,n//2)
                quad(y+n//2,x,n//2)
                quad(y+n//2, x+n//2, n//2)
                print(')', end = '')
                return
    
    if matrix[y][x] == 0:
        print('0',end = '')
        return
    
    else:
        print('1', end = '')
        return

quad(0,0,n)