def solution(s):
    s = s.lower()
    s = list(s.strip())
    
    for i in range(len(s)):
        if i == 0:
            s[i] = s[i].upper()
            
        if s[i] == ' ':
            s[i+1] = s[i+1].upper()
            
    answer = ''.join(s)
    return answer


    