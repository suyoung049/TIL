arr = [1, 2, 3, 100, 99, 98]
def solution(arr):
    for i in range(len(arr)):
        if (arr[i] % 2 == 0):
            if arr[i] >= 50:
                arr[i] = arr[i]//2       
        else:
            if arr[i] < 50:
                arr[i] = arr[i] * 2
                
               
                
    answer = arr
    return answer

solution(arr)