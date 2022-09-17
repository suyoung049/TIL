import sys
sys.stdin = open('2_input.txt', 'r')


T = int(input())

for test_case in range(1, T+1):
    n, m = map(int, input().split())

    water = 1 + (2*m)
    
    print(f'#{test_case}', end = ' ')
    if n % water == 0:
        print(n//water)

    else:
        print(n//water +1)