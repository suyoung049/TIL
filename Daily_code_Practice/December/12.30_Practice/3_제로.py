import sys
sys.stdin = open('3_input.txt')
input = sys.stdin.readline

n = int(input())

stack = []

for i in range(n):
    num_ = int(input())
    if num_ == 0:
        stack.pop()
    else:
        stack.append(num_)

print(sum(stack))