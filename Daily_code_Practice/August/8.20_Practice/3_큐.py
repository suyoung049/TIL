import sys
sys.stdin = open('3_input.txt', 'r')

N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    com = sys.stdin.readline().split()
    if com[0] == 'push':
        stack.append(com[1])
    elif com[0] == 'front':
        if stack:
            print(stack[0])
        else:
            print('-1')
    elif com[0] == 'back':
        if stack:
            print(stack[-1])
        else:
            print('-1')
    elif com[0] == 'size':
        print(len(stack))
    elif com[0] == 'pop':
        if stack:
            print(stack.pop(0))
        else:
            print('-1')
    elif com[0] == 'empty':
        if stack:
            print('0')
        else:
            print('1')
