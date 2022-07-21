import sys

sys.stdin = open("10_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    word = input()

    if word == (word[::-1]):
        print(f'#{test_case} {1}')
    else:
        print(f'#{test_case} {0}')