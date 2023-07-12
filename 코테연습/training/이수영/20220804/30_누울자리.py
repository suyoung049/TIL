import sys

sys.stdin = open("30_input.txt", "r")



N = int(input())
matrix = [list(input()) for _ in range(N)]
a, b = 0, 0
for i in range(N):
   len_a = 0
   len_b = 0
   for j in range(N):
    if matrix[i][j] == '.':
        len_a += 1
    else:
        len_a = 0 
    if len_a == 2:
        a += 1
    
    if matrix[j][i] == '.':
        len_b += 1
    else:
        len_b = 0
    if len_b == 2:
        b += 1
print (a, b)
    
    