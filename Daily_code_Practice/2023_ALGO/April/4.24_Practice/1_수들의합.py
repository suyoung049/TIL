import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

n = int(input())

num_ = 0

for i in range(1, 4294967295):
    num_ += i

    if num_ > n:
        break

print(i-1)
