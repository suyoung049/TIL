# 10 = 9 + 5
# 9 = 8 + 4
# 8 = 7 + 3
# 7 = 6 + 2
# 6 = 5 + 1

import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())

    dp = [0, 1, 1, 1, 2, 2]

    for i in range(6, n+1):
        dp.append(dp[i-1]+dp[i-5])

    print(dp[n])


