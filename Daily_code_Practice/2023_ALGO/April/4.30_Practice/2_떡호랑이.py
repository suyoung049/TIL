import sys
sys.stdin = open("2_input.txt", "r")
input = sys.stdin.readline

day, end = map(int, input().split())

dp = [0] * (day +1)

dp[day] = end
dp[day-1] = (end//2)

while True:
    for i in range(day, 2, -1):
        dp[i-2] = dp[i] - dp[i-1]
        if dp[i-1] > dp[i] or dp[i-1] > dp[i-2]:
            continue
    
    if dp[1] > 0 and dp[2] > dp[1]:
        break

    dp[day-1] += 1

print(dp[1])
print(dp[2])