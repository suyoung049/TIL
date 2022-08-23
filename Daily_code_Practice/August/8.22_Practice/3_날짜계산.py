import sys
sys.stdin = open('3_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())
    sum_ = 0
    while m1 < m2:
        if m1 == 1:
            sum_ = sum_ + 31
            m1 += 1
        elif m1 == 2:
            sum_ = sum_ + 28
            m1 += 1
        elif m1 == 3:
            sum_ = sum_ + 31
            m1 += 1
        elif m1 == 4:
            sum_ = sum_ + 30
            m1 += 1
        elif m1 == 5:
            sum_ = sum_ + 31
            m1 += 1
        elif m1 == 6:
            sum_ = sum_ + 30
            m1 += 1
        elif m1 == 7:
            sum_ = sum_ + 31
            m1 += 1
        elif m1 == 8:
            sum_ = sum_ + 31
            m1 += 1
        elif m1 == 9:
            sum_ = sum_ + 30
            m1 += 1
        elif m1 == 10:
            sum_ = sum_ + 31
            m1 += 1
        elif m1 == 11:
            sum_ = sum_ + 30
            m1 += 1
    sum_ = sum_ + (d2-d1) + 1
    print(f'#{test_case} {sum_}')