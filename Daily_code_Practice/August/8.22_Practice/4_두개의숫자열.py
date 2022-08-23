import sys
sys.stdin = open('4_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    n1_list = list(map(int, input().split()))
    n2_list = list(map(int,input().split()))

    sum_ = 0
    sum_list = []
    for i in range(abs(N-M) + 1):
        for j in range(min(N,M)):
            if len(n1_list) > len(n2_list):
                sum_ += n1_list[j+i]*n2_list[j]
            elif len(n1_list) < len(n2_list):
                sum_ += n1_list[j]*n2_list[j+i]
            else:
                sum_ += n1_list[j]*n2_list[j]
        sum_list.append(sum_)
        sum_ = 0
    print(f'#{test_case}', end = ' ')
    print(max(sum_list))
