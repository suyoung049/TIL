import sys
sys.stdin = open('1_input.txt','r')

T = int(input())

for test_case in range(1, T+1):
    student = int(input())

    group = student//3

    print(f'#{test_case} {group}')