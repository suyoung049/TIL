import sys
sys.stdin = open('6_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]


w_paper = 0
b_paper = 0

def divide(y, x, n):
    global w_paper
    global b_paper

    for j in range(y, y+n):
        for i in range(x, x+n):
            if matrix[y][x] != matrix[j][i]:
                divide(y, x, n//2)
                divide(y+n//2, x, n//2)
                divide(y, x+n//2, n//2)
                divide(y+n//2, x+n//2, n//2)
                return
        
    if matrix[y][x] == 0:
        w_paper += 1

    else:
        b_paper += 1


divide(0,0,n)
print(w_paper)
print(b_paper)


















divide(0, 0, n)