import sys

sys.stdin = open("_파리퇴치.txt")
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
   
    max = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            
            sum_list = 0
            for x in range(M):
                for y in range(M):
                    sum_list += matrix[i+x][j+y]
            print(sum_list)
            if sum_list > max:
                max = sum_list
    print(max)
   
