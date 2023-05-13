import sys
sys.stdin = open("2_input.txt", "r")
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    word_len = int(input())
    if word_len < 2 or word_len%2 != 0:
        print(0)
        continue
    
    catalan = word_len//2

    dp = [0] * (catalan+1)

    dp[0] = 1
    dp[1] = 1 
  
    if catalan >= 2:
        for j in range(2, catalan+1):
            for i in range(1, j+1):
                dp[j] += dp[j-i] * dp[i-1] % 1000000007
    
    print(dp[catalan]%1000000007)
    