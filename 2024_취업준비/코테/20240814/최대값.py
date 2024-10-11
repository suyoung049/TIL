from itertools import combinations

numbers = [1, 2, -3, 4, -5]

def solution(numbers):
    answer = []
    for i in combinations(numbers, 2):
        answer.append(i[0] * i[1])
    
    return max(answer)

solution(numbers)
