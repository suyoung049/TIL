import sys

sys.stdin = open("26_input.txt", "r")
from pprint import pprint
N, M = map(int, input().split())
matrix = []
a, b = 0, 0
gard = 'X'
for _ in range(N):
    line = list(input())
    matrix.append(line)

for i in range(N):
    if gard not in matrix[i]:
        a += 1
    # print(matrix[i])    #['X', 'X', '.', '.', '.']
                          #['.', 'X', 'X', '.', '.']
                          #['.', '.', '.', 'X', 'X']


for j in range(M):
    if gard not in [matrix[i][j] for i in range(N)]:
        b += 1
    print([matrix[i][j] for i in range(N)])    
# ['X', '.', '.']
# ['X', 'X', '.']
# ['.', 'X', '.']
# ['.', '.', 'X']
# ['.', '.', 'X']
   
print(max(a,b))

    

    