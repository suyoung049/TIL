import sys
sys.stdin = open('1_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    print(f'#{test_case}', end =' ')
    if N <= K <=M:
        print(0)

    elif K > M:
        print(-1)
    
    elif K < N:
        print(N-K)
