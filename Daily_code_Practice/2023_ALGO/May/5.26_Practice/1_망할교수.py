import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

subject, score = map(int, input().split())

subject_num = [0]
time = [0]

# 배낭 문제 같은경우 넘겨야 할 기준을 잘 찾고 그 기준은 1부터 주어진 제한(큰수라도) 까지 지정해주는게 중요 (ex. 무게, 시간)
# 밸류 값은 주어진 인덱스로 반복문 돌릴것 (ex 점수, 값)

for _ in range(subject):
    unit, study_time = map(int, input().split())
    subject_num.append(unit)
    time.append(study_time)

dp = [[0] * (subject + 1) for _ in range(score + 1)]

for j in range(1, score+1):
    for i in range(1, subject + 1):
        if j >= subject_num[i]:
            dp[j][i] = max(dp[j][i-1], dp[j-subject_num[i]][i-1] + time[i])

        else:
            dp[j][i] = dp[j][i-1]

print(dp[score][subject])


