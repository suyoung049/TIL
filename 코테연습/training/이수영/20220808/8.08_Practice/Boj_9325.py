import sys

sys.stdin = open("9325_input.txt", "r")

T = int(input())

for test_case in range(T):
    s = int(input())
    n = int(input())
    option_sum = 0
    for _ in range(n):
        q, p = map(int, input().split())
        option = (q * p)
        option_sum += option
    car = s + option_sum
    print(car)