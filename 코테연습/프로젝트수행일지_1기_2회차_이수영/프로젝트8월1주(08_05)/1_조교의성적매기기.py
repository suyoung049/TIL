import sys

sys.stdin = open("_조교의성적매기기.txt")
score_bord = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
T = int(input())
for test_case in range(1, T+1):

    N, M = map(int, input().split())
    score_list =[]
    for _ in range(N):
        a, b, c = map(int, input().split())
        score = (a * 0.35) + (b * 0.45) + (c * 0.2)
        score_list.append(score)
    k_score = score_list[M-1]
    score_list.sort(reverse = True)
    

    value = N//10
    result = score_list.index(k_score) // value
    print(f'#{test_case} {score_bord[result]}')
