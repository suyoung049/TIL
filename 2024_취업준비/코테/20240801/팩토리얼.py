n = 7

def solution(n):
    answer = 0
    
    for i in range(10, 0, -1):
        result = factorial(i)
        if (result <= n):
            
            answer = i
            break
    
    return answer

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


solution(n)