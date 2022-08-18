import sys
sys.stdin = open('3_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):


    M, N = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(M)]
    
    max = 0

    for i in range(0, M-N +1):
        for j in range(0, M-N+1):
            
            fry = 0
            
            for x in range(N):
                for y in range(N):
                    fry += matrix[i+x][j+y]
            
            if fry > max:
                max = fry
    print(f'#{test_case} {max}')



