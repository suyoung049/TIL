import sys
sys.stdin = open("1_input.txt", "r")

def pprint(list_):
    for row in list_:
        print(row)


text_1 = input()
text_2 = input()

len_1 = len(text_1)
len_2 = len(text_2)

answer = 0
text_1 = " " + text_1
text_2 = " " + text_2
dp = [[0] * (len_1 + 1) for _ in range(len_2 + 1)]

for j in range(1, len_2+1):
    for i in range(1, len_1+1):
        if text_2[j] == text_1[i]:
            dp[j][i] = dp[j-1][i-1] + 1
            answer = max(answer, dp[j][i])

print(answer)