import sys
sys.stdin = open('4_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    n = int(input())

    num_list = input().split()
    sum_ = 0

    for num_ in num_list:
        x = int(num_[-1])
        y = int(num_[0:(len(num_)-1)])

        sum_ += (y**x)

    print(f'#{test_case} {sum_}')

