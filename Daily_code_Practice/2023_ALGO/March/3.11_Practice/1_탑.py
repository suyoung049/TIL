import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
tower_list = list(map(int, input().split()))

stack = []
answer = []

for i in range(n):
    if i == 0:
        stack.append((i+1,tower_list[i]))
        answer.append(0)
    
    else:
        if stack[-1][1] < tower_list[i]:
            while True:
                stack.pop()
                
                if len(stack) == 0:
                    stack.append((i+1,tower_list[i]))
                    answer.append(0)
                    break

                if stack[-1][1] > tower_list[i]:
                    answer.append(stack[-1][0])
                    stack.append((i+1,tower_list[i]))
                    break
        
        
        elif stack[-1][1] > tower_list[i]:
            answer.append(stack[-1][0])
            stack.append((i+1,tower_list[i]))

for i in answer:
    print(i, end=' ')