import sys
sys.stdin = open('1_input.txt', 'r')

T = 10

for test_case in range(1, T+1):

    n = int(input())

    bd = list(map(int, input().split()))

    result = 0

    for i in range(2, len(bd)-2):
        max_ = max(bd[i-1], bd[i+1], bd[i-2], bd[i+2])

        if bd[i] > max_:
            result += bd[i] - max_

    print(f'#{test_case} {result}')


        
    


