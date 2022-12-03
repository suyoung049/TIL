import sys
sys.stdin = open('2_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    
    n = list(map(int, input()))
    while True:
        if len(n) == 1:
            print(f'#{test_case} {n[0]}')
            break

        else:
            n = str(sum(n))
            n = list(map(int, n))
    
    

            