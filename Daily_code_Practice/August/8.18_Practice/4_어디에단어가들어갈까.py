import sys 
sys.stdin = open('4_input.txt', 'r')

def pprint(arr):
    for i in range(len(arr)):
        print(arr[i])

T = int(input())

for test_case in range(1,T+1):
    N, K = map(int, input().split())

    matrix = []
    for _ in range(N):
        list_ = list(map(int, input().split()))
        matrix.append(list_)
    coun = 0
    len_ = 0
    for i in range(N):
        
        for j in range(N):
            
            
            
            if matrix[i][j] == 1:
                len_ += 1
            
            if matrix[i][j] == 0 or j == (N-1):
                if len_ == K:
                    coun += 1
                len_ = 0
    len_2 = 0
    for i in range(N):
        
        for j in range(N):
            

           

            if matrix[j][i] == 1:
                len_2 += 1

            if matrix[j][i] == 0 or j == (N-1):
                if len_2 == K:
                    coun += 1
                len_2 = 0
    print(f'#{test_case} {coun}')
            

