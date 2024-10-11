numbers = [1, 2, 3, 4, 5]

def solution(numbers):
    answer = 0
    for i in range(len(numbers)):
        if (numbers[i] == 0):
            continue
        for j in range(i+1,len(numbers)):
            if (numbers[j] == 0):
                continue
            multi = numbers[i] * numbers[j]
            if (answer < multi):
                answer = multi
   
    return answer

solution(numbers)