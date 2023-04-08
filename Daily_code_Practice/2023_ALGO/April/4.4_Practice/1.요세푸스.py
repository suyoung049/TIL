import sys
from collections import deque
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

n, k = map(int, input().split())

num_li = list(range(1, n+1))
q = deque(num_li)
stack = []

i = 1

while True:
    if len(q) == 0:
        break

    if i < k:
        a = q.popleft()
        q.append(a)
        i += 1

    elif i == k:
        a = q.popleft()
        stack.append(a)
        i = 1
    

print('<', end='')
for i in range(n):
    if i == n-1: 
        print(f'{stack[i]}',  end='')
    else:
        print(f'{stack[i]}, ',  end='')
print('>',  end='')