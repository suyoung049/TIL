l =10
r = 20
def solution(l, r):
    answer = []
    for num in range(l, r+1):
        plg = 0
        if num % 5 == 0:
            num_3 = num // 5
            str_num = str(num_3)

            for k in str_num:
                if k == '1' or k == '0':
                    continue
                else:
                    plg = 1
        else:
            plg = 1
        if plg == 0:
            answer.append(num)
                
    if len(answer) == 0:
        answer = [-1]
   
    return answer 

solution(l, r)
