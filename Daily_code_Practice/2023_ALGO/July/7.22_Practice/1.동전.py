import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline


coin, target = map(int, input().split())

coin_list = []

for _ in range(coin):
    coin_list.append(int(input()))

dp = [0] * (target + 1) 
dp[0] = 1

for coin in coin_list:
    for i in range(coin, target + 1):
        dp[i] += dp[i-coin]

print(dp[target])