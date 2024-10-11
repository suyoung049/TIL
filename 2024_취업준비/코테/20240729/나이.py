age = 23

def solution(age):
    answer = ''
    text = 'abcdefghijklmnopqrstuvwxyz'
    str_age = str(age)
    for num in str_age:
        answer += text[int(num)]
    
    print(answer)


solution(age)