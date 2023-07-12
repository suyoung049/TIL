import sys

sys.stdin = open("input_2072.txt", "r")
T = int(input())
n = 0
for test_case in range(1, T +1):
    numbers = list(map(int, input().split()))
    x = []
    n += 1
    for i in numbers:
        if i %2 != 0: # 홀수 일때
            x.append(i)
    print(f'#{n} {sum(x)}')

