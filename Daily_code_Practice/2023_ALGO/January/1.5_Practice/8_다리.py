import sys
sys.stdin = open('8_input.txt', 'r')
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())

    def fact(n):
        f = 1

        for i in range(n):
            f *= (i+1)
        return f 

    print(fact(m)//(fact(n)*fact(m-n)))

    # matrix = [[0]*(m+1) for _ in range(n+1)]
  

    # for j in range(1, n+1):
    #     for i in range(1, m+1):
    #         if j == 1:
    #             matrix[j][i] = i
    #             continue
            
    #         if j == i :
    #             matrix[j][i] = 1
            
    #         if i > j:
    #             matrix[j][i] = matrix[j][i-1] + matrix[j-1][i-1]
    
    # print(matrix[n][m])

            
        






