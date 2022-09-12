import sys
sys.stdin = open('6_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
stair = [0 for i in range(301)]
dp = [0 for i in range(301)]
for j in range(n):
    stair[j] = int(input())

dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
dp[2] = max(stair[1] + stair[2], stair[0] + stair[2])

for i in range(3,n):
    dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i] + stair[i-1] )

print(dp[n-1])


    
    
