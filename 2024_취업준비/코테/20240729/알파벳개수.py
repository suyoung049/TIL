my_string = "Programmers"
def solution(my_string):
    chr_li = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    answer = [0] * 52
    for text in my_string:
        if (text.isupper()):
            idx = chr_li.index(text)
            answer[idx] += 1
        else:
            idx = chr_li.index(text.upper()) + 26
            answer[idx] += 1
    
    return answer
solution(my_string)