citations =  [1,10,11]

def solution(citations):
    answer = 0
    citations.sort()
    level = len(citations)

    while level:
        cnt = 0
        for idx in range(len(citations)):
            if citations[idx] >= level:
                cnt = len(citations) - idx
                break
        if cnt >= level:
            return level
        else:
            level -= 1

    return answer

print(solution(citations))