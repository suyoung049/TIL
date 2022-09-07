import sys
from collections import deque
sys.stdin = open('1_input.txt', 'r')

n, k = map(int, input().split())
num_list = deque([])

for i in range(1, n+1):
    num_list.append(i)

print('<', end = '')
while num_list:
    for _ in range(k-1):
        
        num_list.append(num_list[0])  # 요세푸스는 동그란 원으로 숫자들이 이어져 있기 때문에
        num_list.popleft()             # 처음 숫자가 다시 뒤로 입력된다.
        
    print(num_list.popleft(), end ='')

    if num_list:
        print(', ', end = '')

print('>')

