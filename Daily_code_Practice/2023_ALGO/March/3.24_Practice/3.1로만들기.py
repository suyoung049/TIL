import sys
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

# 결과값 저장 dp 배열 생성
dp = [0] * (n+1)

for i in range(2, n+1):
    # 1을 빼는 과정은 어떠한 수 라도 가능 1보다 적은 수 의 횟수 불러오기
    dp[i] = dp[i-1] + 1

    if i % 3 == 0:
        # 3으로 나눠지는 수이면, 위에서 한 1을 뺀 과정의 횟수와 최소값 비교
        dp[i] = min(dp[i], dp[i//3] + 1)
    
    elif i % 2 == 0:
        # 2로 나눠지는 수도 마찬가지
        dp[i] = min(dp[i], dp[i//2] + 1)

print(dp[n])