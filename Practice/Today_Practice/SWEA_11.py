import sys

sys.stdin = open("11_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    a, b, c, d = map(int, input().split())

    if (a+c) < 12 and (b+d) < 60:
        print(f'#{test_case} {(a+c)} {(b+d)}')

    elif (a+c) > 12 and (b+d) < 60:
        print(f'#{test_case} {((a+c)-12)} {(b+d)}')

    elif (a+c) < 12 and (b+d) > 60:
        print(f'#{test_case} {(a+c)+1} {((b+d)-60)}')

    else:
        print(f'#{test_case} {((a+c+1)-12)} {((b+d)-60)}')

