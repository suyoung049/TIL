import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
num_li = list(map(int, input().split()))

re_num = []
dp = [1] * n

for i in range(n-1,-1,-1):
    re_num.append(num_li[i])


for i in range(n):
    for j in range(i):
        if re_num[i] > re_num[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))