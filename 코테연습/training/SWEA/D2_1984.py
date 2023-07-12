import sys

sys.stdin = open("input_1984.txt", "r")
T = int(input())

for test_case in range(1, T + 1):
    num = list(map(int, input().split()))
    max_ = max(num)
    min_ = min(num)
    middle = num.remove(max_)
    middle = num.remove(min_)
    count = 0
    sum_ = 0
    for i in num:
        count += 1
        sum_ += i
    print(f'#{test_case} {round(sum_/count)}')
