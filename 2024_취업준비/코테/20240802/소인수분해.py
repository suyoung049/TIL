import math
n = 12


def solution(n):
   
    answer = []
    d = 2
    num = int(n ** 0.5)
    while True:
       
        if (n % d == 0):
            n = n//d
            if ( d not in answer):
              answer.append(d)
        else:
            d += 1
        
        if (d > num):
            break
    if n > 1:
        answer.append(n)
    
solution(n)