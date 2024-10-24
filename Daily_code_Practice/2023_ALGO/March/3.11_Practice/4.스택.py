import sys
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    command = input().split()
    if command[0] == 'push':
        stack.append(command[1])
    
    elif command[0] == 'pop':
        if stack:
            pop_1 = stack.pop()
            print(pop_1)
        else:
            print(-1)
    
    elif command[0] == 'size':
        print(len(stack))
    
    elif command[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    
    elif command[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)


