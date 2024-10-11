from collections import Counter
before, after = "allpe", "apple"

def solution(before, after):
    answer = 1
    b_counter = Counter(before)
    a_counter = Counter(after)

    for key in b_counter:
        if (a_counter[key]!= b_counter[key]):
            answer = 0
    return answer


solution(before, after)