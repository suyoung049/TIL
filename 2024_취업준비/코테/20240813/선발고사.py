rank, attendance = [3, 7, 2, 5, 4, 6, 1], [False, True, True, True, True, False, False]

def solution(rank, attendance):
    answer = 0
    length = len(rank)
    true_list = []
    for i in range(length):
        if attendance[i] == True:
            true_list.append(rank[i])
    true_list.sort()
    answer = 10000 * rank.index(true_list[0]) + 100 * rank.index(true_list[1]) + rank.index(true_list[2])
    
    return answer
solution(rank, attendance)