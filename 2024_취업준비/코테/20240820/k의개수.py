from collections import Counter

i, j, k = 1, 13, 1

def solution(i, j, k):
    answer = 0
    for num in range(i, j+1):
        num_counter = Counter(str(num))

        answer += num_counter[str(k)]
            
    

    return answer


solution(i, j, k)