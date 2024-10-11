num_list = [12, 4, 15, 1, 14]

def solution(num_list):
    answer = 0
    count = 0
    for num in num_list:
        num_count = make_one(num)
        count += num_count

        
    return answer

def make_one(num):
    count = 0
    while (num != 1):
        if (num % 2 == 0):
            num = num // 2
            count += 1
        else:
            num = (num -1) // 2
            count += 1
    
    return count
    
solution(num_list)