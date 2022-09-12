import sys
sys.stdin = open('5_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)
print(dp)

for i in range(1,n+1):
    if i == 1:
        dp[i] = 1
    if i == 2:
        dp[i] = 3

    if i > 2:
        dp[i] = dp[i-1] + 2*(dp[i-2])

print(dp[n]%10007)