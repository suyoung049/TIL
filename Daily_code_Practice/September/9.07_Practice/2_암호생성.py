import sys
from collections import deque
sys.stdin = open('2_input.txt', 'r')

T = 10

for test_case in range(1, T+1):
    n = int(input())
    code = list(map(int, input().split()))
    code = deque(code)
    i = 1

    while True:
        data = code.popleft()
        data -= i

        if data <=0:
            code.append(0)
            break

        else:
            code.append(data)
            if i >= 5:
                i = 0
            
            i += 1
    print(f'#{test_case}', end=' ')
    print(*code)