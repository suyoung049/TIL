import sys
from itertools import permutations, combinations
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

n = int(input())
num_li = list(map(int, input().split()))

num_sum = sum(num_li)
result = 0

for n in num_li:
    num_sum -= n
    result += num_sum * n

print(result)