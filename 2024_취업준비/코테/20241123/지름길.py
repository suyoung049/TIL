import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

# 입력받기
n, end = map(int, input().split())
short_load = [tuple(map(int, input().split())) for _ in range(n)]

# 지름길 시작점 기준으로 정렬
short_load.sort()

# 무한대 값 설정
INF = float('inf')
dp = [INF] * (end + 1)
dp[0] = 0  # 시작점 비용은 0

# dp 갱신
for i in range(end + 1):
    # 일반 도로로 이동
    if i > 0:
        dp[i] = min(dp[i], dp[i - 1] + 1)
    
    # 지름길 고려
    for a, b, cost in short_load:
        if i == a and b <= end:
            dp[b] = min(dp[b], dp[a] + cost)

# 결과 출력
print(dp[end])



