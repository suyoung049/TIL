binomial = "43 + 12"

def solution(binomial):
    answer = binomial.split()
    
    if answer[1] == "+":
        result = int(answer[0]) + int(answer[2])
    elif answer[1] == "-":
        result = int(answer[0]) - int(answer[2])
    elif answer[1] == "*":
        result = int(answer[0]) * int(answer[2])
    return result


solution(binomial)