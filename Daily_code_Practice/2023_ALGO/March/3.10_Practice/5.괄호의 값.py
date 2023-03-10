import sys
sys.stdin = open('5_input.txt', 'r')
input = sys.stdin.readline


temp = 1
sum_ = 0
stack = []
check = False

a = list(input().strip())


for i in range(len(a)):
    if a[i] == '(':
        stack.append(a[i])
        temp = temp * 2
    
    elif a[i] == '[':
        stack.append(a[i])
        temp = temp * 3
    
    elif a[i] == ')':
        if len(stack) != 0 and stack[-1] == '(':
            if a[i-1] == '(':
                sum_ += temp
            stack.pop()
            temp = temp//2
        else:
            check = True
            

    elif a[i] == ']':
        if len(stack) != 0 and stack[-1] == '[':
            if a[i-1] == '[':
                sum_ += temp
            stack.pop()
            temp = temp//3
        else:
            check = True

if stack:
    check = True
            

if check == True:
    print(0)

else:
    print(sum_)