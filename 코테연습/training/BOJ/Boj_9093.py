import sys

sys.stdin = open("9093_input.txt", "r")

T = int(input())

for test_case in range(T):
    text = input().split()
    for chr in text:
        print(chr[::-1], end = ' ')
    print()