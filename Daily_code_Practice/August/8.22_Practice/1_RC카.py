import sys
sys.stdin = open('1_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    sum_ = 0
    a = 0
    for _ in range(N):
        comand = input().split()
        if comand[0] == '1':
            a += int(comand[1])
            sum_+= a
        elif comand[0] == '0':
            a = a
            sum_ += a
        elif comand[0] == '2':
            if int(comand[1]) > a:
                a = 0
            else:
                a -= int(comand[1])
                sum_ += a
    print(f'#{test_case} {sum_}')