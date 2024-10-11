arr, flag = [3, 2, 4, 1, 3], 	[True, False, True, False, False]

def solution(arr, flag):
    answer = []
    for i in range(len(arr)):
        if flag[i]:
            for j in range(arr[i]):
                answer.append(arr[i])
        else:
            for j in range(arr[i]):
                answer.pop()
                
    return answer

solution(arr, flag)