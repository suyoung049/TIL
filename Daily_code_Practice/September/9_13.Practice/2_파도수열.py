import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())

    dp = [0] * (n+1)

    for i in range(1,n+1):
        if i == 1:
            dp[i] = 1
        if i == 2:
            dp[i] = 1
        if i == 3:
            dp[i] = 1

        if i > 3:
            dp[i] = dp[i-2] + dp[i-3]
    print(dp[n])