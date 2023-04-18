import sys
sys.stdin = open("1_input.txt", 'r')
input = sys.stdin.readline

n, k = map(int, input().split())

num_ = list(map(int, input().strip()))

stack = []

cheange = 0
for i in range(n):
    if i == 0:
        stack.append(num_[i])
    
    else:
        if stack[-1] > num_[i]:
            cheange += 1
            stack.pop()
            stack.append(num_[i])
        else:
            stack.append(num_[i])
        
        if cheange == k:
            break

if k - cheange == 0:
    print(stack)

else:
    for _ in range(k-cheange):
        stack.pop()

    print(stack) 


            
