import sys

sys.stdin = open("2693_input.txt", "r")

T = int(input())
for test_case in range(T):
    num_list = list(map(int, input().split()))
    sor_list = sorted(num_list)
    print(sor_list[7])