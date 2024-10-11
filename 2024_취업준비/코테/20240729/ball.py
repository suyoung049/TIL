balls, share = 3, 2

def solution(balls, share):
    answer = 0
    n = multiply(balls)
    m = multiply(share)
    minus = multiply(balls-share)

    answer = n//(minus * m)
    print(answer)
    return answer


def multiply(num):
    mul_num = 1
    for i in range(1, num+1):
        mul_num *= i
    
    return mul_num
        


solution(balls, share)

