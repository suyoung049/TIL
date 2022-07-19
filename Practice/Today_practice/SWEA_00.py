import sys

sys.stdin = open("00_input.txt", "r")

T = int(input())
n = 0
for test_case in range(1, T +1):
    a, b = map(int, input().split())
    sha = (a//b)
    rem = (a % b)
    n += 1
    print(f"#{n} {sha} {rem}")