import sys
from itertools import combinations
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

n, m , c = map(int, input().split())
point = list(list(map(int, input().split())) for _ in range(c))

A = list(map(int, input().split()))
B = list(map(int, input().split()))

if n >= m:
    small = m
    list_ = list(range(len(A)))
    group_1 = B
    group_2 = A

else:
    small = n
    list_ = list(range(len(B)))
    group_1 = A
    group_2 = B

result = 0
for j in combinations(list_, small):
    print(j)

    sum_ = 0
    for y in range(small):
        sum_ += point[group_1[y]-1][group_2[j[y]]-1]
    
    result = max(result, sum_)

print(result)
