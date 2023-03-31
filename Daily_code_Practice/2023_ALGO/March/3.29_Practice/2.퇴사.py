import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

day = int(input())


schedule = []

dp = [0] * (day + 1)

for _ in range(day):
    deadline, cost = map(int, input().split())
    schedule.append((deadline, cost))

# 뒤에서 부터 거꾸로
for i in range(day-1, -1, -1):
    # 상담에 필요한 일수가 퇴사일을 넘어가면
    if i + schedule[i][0] > day:
        # 다음날 값 그대로 가져옴
        dp[i] = dp[i+1]
    
    else:
        # 오늘 상담을 안 할 경우와 상담을 할 경우 중 max 값
        dp[i] = max(dp[i+1], dp[i + schedule[i][0]] + schedule[i][1])

print(dp[0])