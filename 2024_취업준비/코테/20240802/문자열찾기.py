myString, pat = "aabbaa", "aaa"

def solution(myString, pat):
    answer = 0
    pat_length = len(pat)
    if pat_length > len(myString):
        return answer
    for i in range(len(myString)-pat_length+1):
        word = myString[i:i+pat_length]
        lower_word = word.lower()
        lower_pat = pat.lower()
        if (lower_word == lower_pat):
            print(lower_word, lower_pat)
            print(1)
            answer = 1
          
    return answer

solution(myString, pat)