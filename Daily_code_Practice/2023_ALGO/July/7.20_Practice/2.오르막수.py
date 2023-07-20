import sys
sys.stdin = open("2_input.txt", "r")
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

n = int(input())

dp = [[0] * 10 for _ in range(n)]


for j in range(n):
    for i in range(10):
        if j == 0:
            dp[j][i] = 1
        else:
            dp[j][i] = (sum(dp[j-1][i:])%1007)   

print(sum(dp[n-1])%10007)