def solution(a, b):
    num_list = [a,b]
    answer = 0
    check_list = [0, 0]
    for i in range(2):
        if num_list[i] % 2 == 0:
            check_list[0] +=1
        else:
            check_list[1] += 1
    if check_list[1] == 2:
        answer = a **2 + b ** 2
    elif check_list[1] == 1:
        answer = 2 * (a + b)
    elif check_list[1] == 0:
        answer = abs(a-b)
    
    return answer