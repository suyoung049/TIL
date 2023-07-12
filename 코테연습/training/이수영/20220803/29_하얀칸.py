import sys

sys.stdin = open("29_input.txt", "r")
from pprint import pprint
matrix = []
for _ in range(8):
    line = list(input())
    matrix.append(line)
pprint(matrix)
coun = 0
for i in range(8):
    for j in range(8):
        if (i + j) %2 == 0 and matrix[i][j] == 'F':
            coun += 1
print(coun) 