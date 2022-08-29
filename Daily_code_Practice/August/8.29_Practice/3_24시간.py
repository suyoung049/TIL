import sys
sys.stdin = open('3_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    a,b = map(int, input().split())

    print(f'#{test_case}', end = ' ')
    if a + b >= 24:
        print((a+b)-24)
    
    else:
        print(a+b)