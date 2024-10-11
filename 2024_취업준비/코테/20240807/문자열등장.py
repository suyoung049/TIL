myString, pat = "banana", "ana"
def solution(myString, pat):
    answer = 0
    length = len(pat)
    for i in range(0, len(myString) + 1 - length ):
        
        if (pat == myString[i:i+length]):
            answer += 1
    
    return answer

solution(myString, pat)