import sys
sys.stdin = open("2_input.txt", "r")
input = sys.stdin.readline

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

dp[0][0] = 1

for j in range(n):
    for i in range(n):
        if dp[j][i] > 0 and matrix[j][i] > 0:
            if 0 <= j + matrix[j][i] < n:
                dp[j + matrix[j][i]][i] += dp[j][i]
            
            if 0<= i + matrix[j][i] < n:
                dp[j][i + matrix[j][i]] += dp[j][i]


print(dp[n-1][n-1])