A, B = "hello", "ohell"

def solution(A, B):
    answer = 0
    length = len(A)
    while True:
        if A == B:
            break
        
        else:
            A = push(A)
            answer += 1

        if answer >= length:
            answer = -1
            break

    return answer


def push(text):
    push_text = ""
    push_text += text[-1]
    for i in range(len(text) - 1):
        push_text += text[i]
    
    return push_text


solution(A, B)