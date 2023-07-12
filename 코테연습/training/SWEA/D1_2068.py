import sys

sys.stdin = open("input_2068.txt", "r")
T = int(input())
n = 0
for test_case in range(1, T +1):
    numbers = list(map(int, input().split()))
    n += 1
    max = 0
    for i in numbers:
        if max <= i:
            max = i
    print(f'#{n} {max}')
