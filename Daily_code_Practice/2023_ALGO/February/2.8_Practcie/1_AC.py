import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    command = list(input().strip())
    n = int(input())
    ac = input()[1:-2].split(',')
    
    q = deque(ac)

    flag = 0

    if n == 0:
        q = []

    for c in command:
        if c == 'R':
            flag += 1

        if c == 'D':
            if len(q) == 0:
                print('error')
                break
            
            else:
                if flag % 2 == 0:
                    q.popleft()
                else:
                    q.pop()

    else:
        if flag % 2 == 0:
            print('['+ ','.join(q) +']')


        else:
            q.reverse()
            print('['+ ','.join(q) +']')