myString, pat = "AAAAaaaa","a"

def solution(myString, pat):
    length = len(pat)
    max_str = ''
    for i in range(0, len(myString) + 1 - length):
        if (pat == myString[i:i+length]):
            if (len(max_str) < len(myString[:i + length])):
                max_str = myString[:i + length]
    print(max_str)
                
            
    return max_str

solution(myString, pat)