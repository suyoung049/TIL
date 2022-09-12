import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

T = int(input())

for _  in range(T):
    n = int(input())

    dp = [0] * (n+1)

    for i in range(1,n+1):
        if i == 1:
            dp[i] = 1  
        
        if i == 2:
            dp[i] = 2
        
        if i == 3:
            dp[i] = 4

        if i > 3:
            dp[i] = (dp[i-1]) + (dp[i-2]) + (dp[i-3])  # 1만 더해주면 된다 , 2만 더해주면 된다, 3만 더해주면된다.

    print(dp[n])

