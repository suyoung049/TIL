import sys

sys.stdin = open("괄호_input.txt", "r") 

T = int(input())
for test_caes in range(T):
    stack = []
    brecket = input()
    for i in brecket:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                print('No')
                break
    else:
        if not stack:
            print('YES')
        else:
            print('No')