array, n = [3, 10, 28], 20

def solution(array, n):
    answer = 0
    max_num = 1000
    for num in array:
        
        if (max_num > abs(num -n)):
            answer = num
            max_num = abs(num -n)
        elif(max_num == abs(num-n)):
            if (answer > num):
                answer = num
    
    return answer
solution(array, n)