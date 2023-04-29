import sys
sys.stdin = open("2_input.txt", "r")
input = sys.stdin.readline

n = int(input())

pack = [0] + list(map(int, input().split()))

dp = [[0] * (n+1) for _ in range(n+1)]

for j in range(1, n+1):
    for i in range(1, j+1):
        dp[j][i] = pack[i] + max(dp[j-i])

print(max(dp[n]))