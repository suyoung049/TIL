my_string = "aAb1B2cC34oOp"

def solution(my_string):
    answer = 0
    for str in my_string:
        if (not str.isalpha()):
            answer += int(str)
    print(answer)
    return answer


solution(my_string)