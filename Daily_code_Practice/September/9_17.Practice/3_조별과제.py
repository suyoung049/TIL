import sys
sys.stdin = open('3_input.txt')

T = int(input())

for test_case in range(1, T+1):
    n = int(input())

    print(f'#{test_case} {n//3}')