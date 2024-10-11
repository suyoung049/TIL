from itertools import combinations

dots = [[1, 4], [9, 2], [3, 8], [11, 6]]

def solution(dots):
    answer = 0
    iter = [0, 1, 2, 3]
    for i in combinations(iter, 2):
        main_dots = []
        remain_dots = []
        for j in range(4):
            if i.__contains__(j):
                main_dots.append(dots[j])
            else:
                remain_dots.append(dots[j])
        a = (main_dots[0][0] - main_dots[1][0]) / (main_dots[0][1] - main_dots[1][1])
        b = (remain_dots[0][0] - remain_dots[1][0]) / (remain_dots[0][1] - remain_dots[1][1])

        if a == b:
            answer = 1
            break
        
    return answer


solution(dots)