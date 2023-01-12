import sys
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

text = input()
stack = []

check = ['P', 'P', 'A', 'P']

for i in range(len(text)):
    stack.append(text[i])

    if len(stack) >= len(check):
        if stack[-len(check):] == check:
            for _ in range(4):
                stack.pop()
            
            stack.append('P')

if stack == ['P']:
    print('PPAP')

else:
    print('NP')