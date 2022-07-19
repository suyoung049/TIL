import sys

sys.stdin = open("03_input.txt", "r")
T = int(input())
n = 0
for test_case in range(1, T +1):
    a, b = (map(int, input().split()))
    n += 1
    if a > b:
        print(f"#{n} {'>'}")
    elif a < b:
        print(f"#{n} {'<'}")
    else:
        print(f"#{n} {'='}")
    