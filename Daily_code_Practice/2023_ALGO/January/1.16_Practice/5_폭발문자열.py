import sys
sys.stdin = open('5_input.txt', 'r')
input = sys.stdin.readline

text = input().strip()
check = list(input().strip())
stack = []
j = len(check)

for i in range(len(text)):
    stack.append(text[i])

    if len(stack) >= j:
        if stack[-j:] == check:
            for _ in range(j):
                stack.pop()

if len(stack) == 0:
    print('FRULA')
else:
    answer = ''
    for i in stack:
        answer += i
    print(answer)
