import sys
sys.stdin = open('5_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

num_li = list(map(int, input().split()))
soldier = []
dp = [1] * n

for i in range(len(num_li)-1, -1, -1):
    soldier.append(num_li[i])


for j in range(n):
    for k in range(j):
        if soldier[k] < soldier[j]:
            dp[j] = max(dp[j], dp[k]+1)


best = max(dp)
print(n-best)