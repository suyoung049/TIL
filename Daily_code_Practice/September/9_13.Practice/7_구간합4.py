import sys
sys.stdin = open('7_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())

num_list = list(map(int, input().split()))
dp = [0] * (n)

for i in range(n):
    if i == 0:
        dp[i] = num_list[i]
    if i == 1:
        dp[i] = num_list[i] + num_list[i-1]
    if i > 1:
        dp[i] = num_list[i] + dp[i-1]

for _ in range(m):
    x , y = map(int, input().split())
    x, y = x-1, y-1

    if x == 0:
        print(dp[y])
    
    elif x == y:
        print(num_list[x])

    else:
        print(dp[y]-dp[x-1])


