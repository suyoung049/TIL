def solution(price, money, count):
    pay = 0
    for i in range(1,count+1):
        pay += price * i
        
    if pay <= money:
        answer = 0
    else:
        answer = (pay-money)
        

    return answer