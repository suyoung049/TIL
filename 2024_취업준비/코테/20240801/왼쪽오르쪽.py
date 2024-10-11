str_list = ["u", "u", "l", "r"]

def solution(str_list):
    answer = []
    for str in str_list:
        if (str == "l"):
            answer = str_list[:str_list.index(str)]
            
        elif (str == "r"):
            answer = str_list[str_list.index(str):]
    return answer

solution(str_list)