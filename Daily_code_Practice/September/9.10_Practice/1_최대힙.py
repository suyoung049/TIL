import sys
from collections import deque
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

num_list = [0]
num_list = deque(num_list)

for _ in range(n):
    command = int(input())
    

    if command == 0:
        if num_list:
            while num_list:
                max_ = max(num_list)
                x = num_list.popleft()

                if max_ == x:
                    print(x)
                    break
                else:
                    num_list.append(x)
        else:
            print(0)            

    else:
        num_list.append(command)

