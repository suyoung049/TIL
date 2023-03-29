import sys
sys.stdin = open('2_input.txt', 'r')

def pprint(list_):
    for row in list_:
        print(row)

def find_sentence(y, x, re_dp, second_sentence):
    if y == 0 or x == 0:
        return ''
    
    elif re_dp[y][x] == 1:
        return find_sentence(y-1, x-1, re_dp, second_sentence) + second_sentence[y]
    
    elif re_dp[y][x] == 2:
        return find_sentence(y, x-1, re_dp, second_sentence)
    
    elif re_dp[y][x] == 3:
        return find_sentence(y-1, x, re_dp, second_sentence)

first_sentence = ' ' + input()
second_sentence = ' ' + input()

n, m = len(first_sentence), len(second_sentence)

dp = [[0]*n for _ in range(m)]
re_dp = [[0]*n for _ in range(m)]

for j in range(1, m):
    for i in range(1, n):
        if second_sentence[j] == first_sentence[i]:
            dp[j][i] = dp[j-1][i-1] + 1
            re_dp[j][i] = 1

        elif second_sentence[j] != first_sentence[i]:
            dp[j][i] = max(dp[j-1][i], dp[j][i-1])
            if dp[j-1][i] > dp[j][i-1]:
                re_dp[j][i] = 3
            else:
                re_dp[j][i] = 2


print(dp[m-1][n-1])

print(find_sentence(m-1, n-1, re_dp, second_sentence))