import sys
from collections import deque
sys.stdin = open('7_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
que = deque([])

for _ in range(n):
    command = input().split()

    if command[0] == 'push':
        que.append(command[1])
    
    elif command[0] == 'pop':
        if not que:
            print(-1)
        else: 
            pop_num = que.popleft()
            print(pop_num)
    elif command[0] == 'size':
        print(len(que))
    
    elif command[0] == 'empty':
        if not que:
            print(1)
        else:
            print(0)
    
    elif command[0] == 'front':
        if not que:
            print(-1)
        else:
            print(que[0])
    
    elif command[0] == 'back':
        if not que:
            print(-1)
        else:
            print(que[-1])

