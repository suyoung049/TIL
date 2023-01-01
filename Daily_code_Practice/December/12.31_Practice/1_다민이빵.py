import sys
sys.stdin = open('1_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    a, b, c = map(int, input().split())

    bread = min(a, b)

    print(f'#{test_case} {c//bread}')
