import sys
sys.stdin = open('1_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    n, a, b = map(int, input().split())

    print(f'#{test_case}', end=' ')

    if a == b:
        print(a, b)

    else:
        max_ = min(a,b)
        min_ = (a+b) -n
        if min_ < 0:
            min_=0
        else:
            min_ = (a+b)-n
        print(max_,min_)