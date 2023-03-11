import sys
sys.stdin = open('6_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    num_ = int(input())

    while True:
        if not stack or stack[-1] > num_:
            break
        stack.pop()
    
    stack.append(num_)

print(len(stack))