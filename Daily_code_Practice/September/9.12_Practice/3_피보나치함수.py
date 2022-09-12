import sys
sys.stdin = open('3_input.txt' , 'r')
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())

    dp = [(0,0)]*(n+1)

    for i in range(n+1):
        if i == 0:
            dp[i] = (1,0)

        if i == 1:
            dp[i] = (0,1)

        if i > 1:
            dp[i] = (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1])
    
    print(*dp[n])