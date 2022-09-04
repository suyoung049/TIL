import sys
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

text = input().strip()

ppap = ['P', 'P', 'A', 'P']

stack = []
check = []

for chr in text:
    stack.append(chr)

    if len(stack) >= len(ppap):
        if stack[-len(ppap):] == ppap:
            for _ in range(4):
                stack.pop()
            stack.append('P')    

if stack == ["P"]:
    print('PPAP')

else:
    print('NP')
