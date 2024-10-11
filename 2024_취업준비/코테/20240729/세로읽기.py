my_string, m, c = "ihrhbakrfpndopljhygc",4, 2

def solution(my_string, m, c):
    answer = ''
    text_li = []
    idx = 0
    cnt = (len(my_string)//m)
    for i in range(cnt):
        text = my_string[idx:idx+m]
        text_li.append(text)
        idx = idx + m
    for te in text_li:
        answer += te[c-1]
    print(answer)
        

solution(my_string, m, c)