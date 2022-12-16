import sys
sys.stdin = open('1_input.txt', 'r')

T = 6

for test_case in range(1, T+1):
    n = int(input())

    print(f'#{test_case}', end = ' ')

    if n % 2 == 0:
        print('Alice')
    else:
        print('Bob')