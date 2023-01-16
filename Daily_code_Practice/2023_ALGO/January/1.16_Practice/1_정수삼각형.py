import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

tri = list(list(map(int, input().split())) for _ in range(n))

dp = []

for i in range(1, n+1):
    dp.append([0]*i)

for i in range(n):
    for j in range(len(tri[i])):
        if (i, j) == (0, 0):
            dp[i][j] = tri[i][j]
        
        elif j == 0:
            dp[i][j] = dp[i-1][j] + tri[i][j]
        
        elif j == len(tri[i])-1:
            dp[i][j] = dp[i-1][j-1] + tri[i][j]
        
        elif  0 < j < len(tri[i])-1:
            dp[i][j] = max(dp[i-1][j-1] + tri[i][j], dp[i-1][j] + tri[i][j])

print(max(dp[n-1]))