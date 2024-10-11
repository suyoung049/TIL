score = [[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]

def solution(score):
    answer = [0 for _ in range(len(score))]
    ave_list = []
    for i in range(len(score)):
        average = (score[i][0] + score[i][1]) // 2
        
        ave_list.append((average, i))
    
    sort_ave = sorted(ave_list, key=lambda x:-x[0])
    rank = 1
    change_rank = 1
    for i in range(len(sort_ave)):
        if i == 0:
            answer[sort_ave[i][1]] = rank
        else:
            if sort_ave[i][0] == sort_ave[i-1][0]:
                answer[sort_ave[i][1]] = rank
                change_rank += 1

            else:
                change_rank += 1
                rank = change_rank
                answer[sort_ave[i][1]] = rank
                
    return answer


solution(score)