import sys
sys.stdin = open("3_input.txt", "r")

n = input()

stack = []
stack.append(n[0])
high = 10


for i in range(1, len(n)):
    if n[i] == stack[-1]:
        high += 5
        stack.append(n[i])
    else:
        high += 10
        stack.append(n[i])
print(high)