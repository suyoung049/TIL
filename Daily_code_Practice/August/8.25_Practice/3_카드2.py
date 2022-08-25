import sys
sys.stdin = open('3_input.txt', 'r')




n = int(input())
stack = []

for i in range(n,0,-1):
    stack.append(i)

while True:
    if len(stack) == 1:
        break
    else:
        pop = stack.pop()
        pop_ = stack.pop()
        stack.insert(0, pop_)

print(*stack)

from collections import deque

N = int(input())
deque = deque([i for i in range(1, N+1)])

while(len(deque) >1):
    deque.popleft()
    move_num = deque.popleft()
    deque.append(move_num)
    
print(deque[0])


        