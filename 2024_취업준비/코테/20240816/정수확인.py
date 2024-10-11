def solution(my_string):
    answer = 0
    number = ""
    for i in range(len(my_string)):
        if (not my_string[i].isalpha()):
            number += my_string[i]
            if i == len(my_string) -1:
                answer += int(number)
        else:
            if not number:
                continue
            else:
                answer += int(number)
                number = ""
   
    return answer

solution(my_string="R9")