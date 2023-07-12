import sys

sys.stdin = open("2776_input.txt", "r")
input = sys.stdin.readline
T = int(input())
for test_case in range(T):
    N = int(input())
    rem = set(map(int, input().split()))
    M = int(input())
    num_ = list(map(int, input().split()))
    for number in num_:
        if number in rem:
            print(1)
        else:
            print(0)