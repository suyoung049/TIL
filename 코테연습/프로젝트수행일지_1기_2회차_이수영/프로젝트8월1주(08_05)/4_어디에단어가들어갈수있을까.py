import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")
T = int(input())
for test_case in range(1, T+1):

    N, M = map(int, input().split())
    matrix = [list(input().split()) for _ in range(N)]
    
    a, b = 0, 0
    for i in range(N):
        len_a = 0  
        for j in range(N):
            if matrix[i][j] == '1':
                len_a += 1
            if matrix[i][j] == '0' or j == N-1:
                if len_a == M:
                    a += 1
                len_a = 0
    
    for i in range(N):
        len_b = 0
        for j in range(N):
            if matrix[j][i] == '1':
                len_b += 1
            if matrix[j][i] == '0' or j == N-1:
                if len_b == M:
                    b += 1
                len_b = 0
    print(f'#{test_case} {a+b}')