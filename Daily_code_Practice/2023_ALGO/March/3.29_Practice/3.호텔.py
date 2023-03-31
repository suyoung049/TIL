import sys
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

# C + 100 명으로 하는 이유는 dp에서 C명에 대한 최소비용을 출력할 때, C명보다 많은 고객 수에서
# 최소비용이 나올 수 있기 때문입니다. 100으로 하는 이유는 홍보로 얻을 수 있는 고객의 수가 100을 넘지 않기 때문입니다.

people, city = map(int, input().split())

advertise = []

for _ in range(city):
    cost, adver_people = map(int, input().split())
    advertise.append((cost, adver_people))

INF = sys.maxsize

advertise.sort()

dp = [0] + [INF] * (people + 100)

answer = INF

for y, x in advertise:
    for i in range(x, len(dp)):
        dp[i] = min(dp[i-x] + y, dp[i])

        if i >= people:
            answer = min(answer, dp[i]) 
            

print(answer)