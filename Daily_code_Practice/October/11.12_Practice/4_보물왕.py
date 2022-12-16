import sys
sys.stdin = open('4_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    n = int(input())

    num_ = list(map(int, input().split()))

    if n == 1:
        result = num_[0] * num_[0]

    else:
        result = max(num_) * min(num_)

    
    print(f'#{test_case} {result}')
