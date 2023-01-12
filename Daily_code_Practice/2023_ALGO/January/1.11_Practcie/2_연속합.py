import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))


dp = [a[0]]

for i in range(len(a)-1):
    # dp에 i 번째 수와 i 번까지 더 한 수 중에 더 큰 수 를 저장해준다.
    dp.append(max(dp[i]+a[i+1], a[i+1]))


print(a)
print(dp)