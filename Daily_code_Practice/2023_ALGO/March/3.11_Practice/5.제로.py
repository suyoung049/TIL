import sys
sys.stdin = open('5_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    cost = int(input())

    if cost == 0:
        stack.pop()
    
    else:
        stack.append(cost)

print(sum(stack))