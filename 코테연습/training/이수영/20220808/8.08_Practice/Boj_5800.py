import sys

sys.stdin = open("5800_input.txt", "r")
T = int(input())

for test_case in range(1, T+1):

    score = list(map(int, input().split()))
    score_pop = score.pop(0)
    
    max_score = max(score)
    min_score = min(score)

    sor_score = sorted(score, reverse = True)
    sum_ = 0
    for i in range(len(sor_score)-1):
        if sor_score[i] - sor_score[i+1] > sum_:
            sum_ = sor_score[i] - sor_score[i+1]
    print(f'Class {test_case}')
    print(f'Max {max_score}, Min {min_score}, Largest gap {sum_}')



