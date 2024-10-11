my_string, s, e = "Progra21Sremm3",6, 12

def solution(my_string, s, e):
    first_text = my_string[0:s]
    text = my_string[s:e+1]
    last_text = my_string[e+1::]
    re_text = ''.join(reversed(text))
   
    answer = first_text + re_text + last_text
  
    return answer
    

solution(my_string, s, e)