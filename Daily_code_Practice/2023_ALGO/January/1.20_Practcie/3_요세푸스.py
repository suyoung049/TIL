import sys
from collections import deque
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())

num_list = list(range(1, n+1))

num_list = deque(num_list)


print('<' ,end='')

while num_list:
    for _ in range(m-1):
        num_list.append(num_list[0])
        num_list.popleft()
    print(num_list.popleft(), end='')

    if num_list:
        print(',', end=' ')

print('>')



