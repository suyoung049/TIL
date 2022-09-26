import sys
from math import sqrt   # 제곱근을 나타내는 import
sys.stdin = open('3_input.txt', 'r')

T = int(input())


for test_case in range(1, T+1):
    result = 0
    a, b = map(int, input().split())

    for i in range(a,b+1):
        if str(i) == str(i)[::-1]:
            value = sqrt(i)

            if value == int(value):

                if str(int(value)) == str(int(value))[::-1]:
                   
                    result += 1

    print(f'#{test_case} {result}')
    print(T)