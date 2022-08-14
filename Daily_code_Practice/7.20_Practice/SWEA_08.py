import sys

sys.stdin = open("08_input.txt", "r")

T = int(input())
n = 0
for test_case in range(1, T+1):
    p, q, r, s, w = map(int, input().split())
    A_use = (w*p)
    n += 1
    if w <= r:
        B_use = q
    else:
        B_use = (q + ((w-r)*s))

    if A_use > B_use:
        print(f'#{n} {B_use}')
    else:
        print(f'#{n} {A_use}')