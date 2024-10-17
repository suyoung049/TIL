brown, yellow = 24, 24

def solution(brown, yellow):
    candidate = num_list(yellow)

    for y,x in candidate:
        total = (y * 2) + (x * 2) + 4
        if brown == total:
            answer = [y + 2, x +2]
    
    answer.sort(reverse=True)
    
    return answer


def num_list(yellow):
    limit = int(yellow ** 0.5)
    candidate = []

    for i in range(1, limit + 1):
        if yellow % i == 0:
            candidate.append((i, yellow//i))
    
    return candidate


print(solution(brown, yellow))