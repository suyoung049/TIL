q, r, code = 3, 1, "qjnwezgrpirldywt"

def solution(q, r, code):
    answer = ''
    length = len(code)
    for i in range(length):
        if (i % q == r):
            answer += code[i]
    print(answer)
    return answer

solution(q, r, code)