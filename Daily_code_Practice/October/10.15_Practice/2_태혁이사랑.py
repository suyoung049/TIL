import sys
sys.stdin = open('2_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    d, h, m = map(int, input().split())

    minute = m-11
    hour = h -11
    day = d-11

    if minute < 0:
        hour -= 1
        minute += 60

    if hour < 0:
        day -= 1
        hour += 24

    print(f'#{test_case}', end = ' ')

    if day < 0:
        print(-1)

    else:
        print(minute + (day*24 + hour)*60)