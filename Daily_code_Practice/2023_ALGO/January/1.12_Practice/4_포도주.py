import sys
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

grap = [0]
dp = [0] * (n+1)

for _ in range(n):
    a = int(input())
    grap.append(a)

for i in range(1,n+1):
    if i == 1:
        dp[i] = grap[i]

    if i == 2:
        dp[i] = grap[1] + grap[2]

    
    # 이번 문제는 저번 계단오르기와 달리 자기 차례를 하지 않는 경우의 수도 포함시켜야 한다. 본인이 포함되지 않을 경우 전의 잔의 dp값이 이에 해당된다.
    if i > 2:
        dp[i] = max(grap[i] + dp[i-2], grap[i]+grap[i-1] + dp[i-3], dp[i-1])

print(dp[n])


