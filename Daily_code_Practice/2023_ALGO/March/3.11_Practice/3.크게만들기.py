import sys
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

n, k = map(int, input().split())

num_li = list(input().strip())
stack = []

for i in range(len(num_li)):
    if k == 0:
        stack.append(num_li[i])
    
    if i == 0:
        stack.append(num_li[i])
    
    else:
        if stack[-1] < num_li[i]:
            while True:
                stack.pop()
                k -= 1

                if len(stack) == 0 or k == 0:
                    stack.append(num_li[i])
                    break
                
                elif stack[-1] >= num_li[i] and k:
                    stack.append(num_li[i])
                    break
                
        elif stack[-1] >= num_li[i] and k:
            stack.append(num_li[i])

if k == 0:
    print(''.join(stack))
else:
    print(''.join(stack[:-k]))