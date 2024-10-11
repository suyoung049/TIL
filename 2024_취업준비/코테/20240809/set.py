arr, k = [0, 1, 1, 2, 2, 3], 3

def solution(arr, k):
    answer = []
    for num in arr:
        if len(answer) == k:
            continue
        if answer.__contains__(num):
            continue
        else:
            answer.append(num)
    
    if len(answer) < k:
        for j in range(k - len(answer)):
            answer.append(-1)
    return answer
            

solution(arr, k)