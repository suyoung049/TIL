emergency = [3, 76, 24]

def solution(emergency):
    answer = []
    sr_em = sorted(emergency, reverse=True)
    for em in emergency:
        answer.append(sr_em.index(em) + 1)
    print(answer)
    
    return answer

solution(emergency)