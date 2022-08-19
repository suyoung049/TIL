import sys
sys.stdin = open('2_input.txt', 'r')

n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    com = sys.stdin.readline().split()
    if com[0] == 'push':
        stack.append(com[1])
    elif com[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print('-1')
    elif com[0] == 'size':
        print(len(stack))
    elif com[0] == 'empty':
        if not stack:
            print('1')
        else:
            print('0')
    elif com[0] == 'pop':
        if stack:
            pop = stack.pop()
            print(pop)
        else:
            print('-1')
    