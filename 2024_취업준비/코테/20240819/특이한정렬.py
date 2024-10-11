numlist, n = [1, 2, 3, 4, 5, 6], 4

def solution(numlist, n):
    new_num = []
    for num in numlist:
        new_num.append((abs(num-n), num-n, num))
    sort_num = sorted(new_num, key=lambda x:(x[0], -x[1]))
    answer = []
    for i in range(len(sort_num)):
        answer.append(sort_num[i][2])
    return answer

solution(numlist, n)