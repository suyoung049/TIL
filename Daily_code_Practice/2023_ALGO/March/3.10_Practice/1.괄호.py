import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

for _ in range(n):

    stack = []
    a = list(input().strip())
   
    for i in a:
        if i == '(':
            stack.append(i)
        
        else:
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
        
    if stack:
        print('NO')

    else:
        print('YES')


   