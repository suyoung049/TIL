n = 1000

# 문제에서 주어진 나누어줄 값

# 피사노 주기는 피보나치 수를 K로 나눈 나무지는 항상 주기를 갖게 된다는 원리

mod = 1000000
dp = [0, 1]

# 주기의 길이가 P일때 , N번째 피보나치 수를 M으로 나눈 나머지는 N%P번째 피보나치 수를 M으로 나눈 나머지와 같습니다.
# mod = 10^K일 때(중요), K>2 라면, 주기는 항상 15 * 10^(k-1)입니다.
p = (mod//10) * 15

for i in range(2, p):
    dp.append(dp[i-1] + dp[i-2])
    dp[i] %= mod

print(dp[n%p])