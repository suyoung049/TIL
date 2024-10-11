from copy import deepcopy

n, info = 1, [1,0,0,0,0,0,0,0,0,0,0]
score_board = []
score_gap = 0

def compare(past, new):
    flag = 0
    for i in range(10, -1, -1):
        if new[i] > past[i] and flag == 0:
            flag = 1
            return True
        elif new[i] < past[i] and flag == 0:
            flag = 1
            return False
        
def dfs(n, score, info, ryan):
    global score_board
    global score_gap
    r_score, a_score = 0, 0
    # 함수가 중단되는 경우
    # 1. 모든 화살을 전부 쏜 경우
    # 2. 점수가 0점인 경우
    if (n == 0 or score == 0):
        if (score == 0 and n > 0):
            ryan[10] = n
        for i in range(11):
            # 둘다 과녁에 맞춘 경우가 0일 경우
            if info[i] == 0 and ryan[i] == 0:
                continue
            elif info[i] >= ryan[i]:
                a_score += 10 - i
            elif info[i] < ryan[i]:
                r_score += 10 - i
        gap = r_score - a_score
        if gap > score_gap:
            score_gap = gap
            score_board = ryan
        elif gap == score_gap and score_gap != 0:
            temp_score = deepcopy(score_board)
            if compare(temp_score, ryan):
                score_board = ryan        
        return
    idx = 10 - score
    #ryan이 점수를 얻는 경우
    if (n > info[idx]):
        temp = deepcopy(ryan)
        temp[idx] = info[idx] + 1
        dfs(n-info[idx]-1, score-1, info, temp)
    #ryan이 점수를 얻지 못하는 경우
    temp = deepcopy(ryan)
    dfs(n, score-1, info, temp)

def solution(n, info):
    answer = 0
    ryan = [0 for _ in range(11)]
    dfs(n, 10, info, ryan)
    if (len(score_board) == 0):
        return [-1]
    print(score_board)
    return score_board

solution(n, info)