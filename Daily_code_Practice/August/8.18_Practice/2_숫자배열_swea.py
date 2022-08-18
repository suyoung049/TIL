import sys

sys.stdin = open("2_input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]
    d_270 = [[0] * N for _ in range(N)]
    d_90 = [[0] * N for _ in range(N)]
    d_180 = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            d_270[i][j] = a[j][(N-1)-i]
            d_90[i][j] = a[(N-1)-j][i]
            d_180[i][j] = a[(N-1)-i][(N-1)-j]
    print(f'#{test_case}')

    for i in range(N):
        print(''.join(map(str, d_90[i])), end = ' ')
        print(''.join(map(str, d_180[i])), end = ' ')
        print(''.join(map(str, d_270[i])), end = ' ')
        
        print()