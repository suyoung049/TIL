import sys
sys.stdin = open('2_input.txt', "r")
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

n = int(input())
train = list(map(int, input().split()))
limit = int(input())

train_sum = [0]
for t in train:
    t_sum = train_sum[-1] + t
    train_sum.append(t_sum)

dp = [[0] * (n+1) for _ in range(4)]

for j in range(1, 4):
    for i in range(j*limit , n+1):
        if j == 1:
            dp[j][i] = max(dp[j][i-1], train_sum[i] - train_sum[i-limit])
        else:
            dp[j][i] = max(dp[j][i-1], dp[j-1][i-limit] + train_sum[i] - train_sum[i-limit])

print(dp[3][n])