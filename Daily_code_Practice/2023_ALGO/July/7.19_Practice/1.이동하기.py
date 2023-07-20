import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

n, m = map(int, input().split())

dp = [[0] * (m+1) for _ in range(n+1)]

matrix = [list(map(int, input().split())) for _ in range(n)]

for j in range(n):
    for i in range(m):
        dp[j+1][i+1] = matrix[j][i]


for j in range(1, n+1):
    for i in range(1, m+1):
        dp[j][i] = dp[j][i] + max(dp[j-1][i-1], dp[j-1][i], dp[j][i-1])


print(dp[n][m])