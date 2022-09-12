import sys
sys.stdin = open('9_input.txt')
input = sys.stdin.readline

n = int(input())

hash = list(input().strip())
code = []
for i in range(n):
    x = ord(hash[i]) -  96
    code.append(x)

sum_ = 0
for y in range(n):
    sum_ += code[y] * (31**(y))

print(sum_%1234567891)

    