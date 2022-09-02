import sys
sys.stdin = open('2_input.txt', 'r')

for _ in range(10):
    T = int(input())
    N, M = map(int,input().split())

    def power(N, M):
        if M == 0:
            return(1)
        
        else:
            return(N*power(N,M-1))

    print(f'#{T} {power(N,M)}')