import sys
from collections import deque
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

# text = input().split()
# stack = ''

# for i in range(len(text)):
#     q = deque()
#     for j in range(len(text[i])):
#         q.append(text[i][j])
    
#     chr = q.popleft()
    
#     if chr.isupper() == True:
#         stack += chr

# if stack[:4] == 'UCPC':
#     print('I love UCPC')
# else:
#     print('I hate UCPC')

text = input().replace(' ', '')
answer = 'UCPC'
idx = 0

for i in text:
    if i == answer[idx]:
        idx += 1
    
    if idx == 4:
        print('I love UCPC')
        break

else:
    print('I hate UCPC')
    



