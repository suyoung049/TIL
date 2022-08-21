import sys
sys.stdin = open('2_input.txt','r')

T = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-','D0']
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    score_list = []
    for _ in range(N):
        a, b, c = map(int, input().split())
        score = (a*0.35) + (b*0.45) + (c*0.2)
        score_list.append(score)
    M_score = score_list[M-1]
    sor_list = sorted(score_list, reverse = True)
    
    k = N//10
    num_ = sor_list.index(M_score)
    result = grade[num_//k]
    print(f'#{test_case} {result}')
   

