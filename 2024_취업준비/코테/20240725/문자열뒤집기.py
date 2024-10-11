my_string = "hello"
n = 3

def solution(my_string, n):
    answer = ''
    for st in my_string:
        answer += st * n
        
    
    
    return answer


solution(my_string, n)