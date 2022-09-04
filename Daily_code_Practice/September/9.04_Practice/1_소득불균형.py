import sys
sys.stdin = open('1_input.txt', 'r')

T = int(input())

for test_case in range(1,T+1):
    n = int(input())

    people = list(map(int, input().split()))

    money = sum(people)/n

    count = 0

    for i in people:
        if money >= i:
            count += 1

    print(f'#{test_case} {count}' )