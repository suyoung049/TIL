from collections import Counter
s = "abcabcadc"
def solution(s):
    answer = []
    str_count = Counter(s)
    for key in str_count:
        if str_count[key] == 1:
            answer.append(key)
    answer.sort()
    result = "".join(answer)
    print(result)

    return result
        
  
solution(s)