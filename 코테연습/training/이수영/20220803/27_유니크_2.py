import sys

sys.stdin = open("27_input.txt", "r")

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
score_list = []
for j in range(3):
    test = [matrix[i][j] for i in range(N)]
    score_list.append(test)
print(score_list)
sum_ = [0] * 5

for j in range(3):
    score_line = score_list[j]
    for i in range(N):
        score = score_line[i]
        if score_line.count(score) == 1:
            sum_[i] += score
for score in sum_:
    print(score)
    

