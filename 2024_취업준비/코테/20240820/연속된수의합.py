num, total = 5, 15

def solution(num, total):
    answer = []
    i = 0

    start = (total - num_sum(num)) // num
    while (i < num):
        answer.append(start + i)
        i += 1
        
    return answer

def num_sum(num):
    total = 0
    for i in range(num):
        total += i

    return total


solution(num, total)