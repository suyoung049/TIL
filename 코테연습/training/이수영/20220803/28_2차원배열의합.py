
import sys

sys.stdin = open("28_input.txt", "r")
from pprint import pprint

N, M = map(int, input().split())
matrix = []
for _ in range(N):
    line = list(map(int, input().split()))
    matrix.append(line)
T = int(input())

for test_case in range(T):
    a, b, x, y = map(int, input().split())
    count = 0
    for i in range(a-1, x):
        for j in range(b-1, y):
            count += matrix[i][j]
    print(count)

# 이 코드는 계속 시간초과가 나오는 코드 다른 알고리즘 접근 필요!!

