import sys
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

text = input().strip()
stack = []


for i in range(len(text)):
    stack.append(text[i])

    if len(stack) >= 4:
        if stack[-4:] == ['P', 'P', 'A', 'P']:
            for _ in range(4):
                stack.pop()
            
            stack.append('P')

if stack == ['P']:
    print('PPAP')
else:
    print('NP')