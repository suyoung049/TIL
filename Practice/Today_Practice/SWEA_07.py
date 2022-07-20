import sys

sys.stdin = open("07_input.txt", "r")

T = int(input())
n = 0
for test_case in range(1, T +1):
    a = input()
    n = int(a)
    y = 0
    for i in range(0, n+1):
        y = y -(i*((-1)**i))
    print(f'#{n} {y}')
