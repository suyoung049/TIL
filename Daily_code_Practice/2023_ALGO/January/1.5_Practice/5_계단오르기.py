import sys
sys.stdin = open('5_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

stair = [0] * (301)
dp = [0] * (301)

for i in range(1, n+1):
    stair[i] = int(input())


dp[1] = stair[1]
dp[2] = stair[2] + stair[1]


for i in range(3, n+1):
    dp[i] = max(stair[i] + dp[i-2] , stair[i] + stair[i-1] + dp[i-3])

print(dp[i])