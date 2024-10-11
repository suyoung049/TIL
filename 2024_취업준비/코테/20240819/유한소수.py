a, b = 12, 21

def solution(a, b):
    answer = 2
    gcd_num = gcd(a, b)
    b_num = b//gcd_num

    while True:
        if (b_num%2 == 0 or b_num % 5== 0):
            if b_num % 2 == 0:
                b_num = b_num//2
            else:
                b_num = b_num//5
        
        else:
            break
    if b_num == 1:
        answer = 1
        
    return answer

def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i


solution(a, b)