num, k = 29183, 1

def solution(num, k):
    answer = 0
    str_num = str(num)
    answer = str_num.index(str(k)) + 1
    return answer

solution(num, k)