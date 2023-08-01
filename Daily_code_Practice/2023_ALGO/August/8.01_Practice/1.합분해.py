import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [[0] * (n+ 1) for _ in range(k+1)]

for j in range(1, k+1):
    for i in range(n+1):
        if j == 1:
            dp[j][i] = 1
        elif i == 0:
            dp[j][i] = 1
        
        else:
            dp[j][i] = (dp[j-1][i] + dp[j][i-1]) % 1000000000

print(dp[k][n] % 1000000000)