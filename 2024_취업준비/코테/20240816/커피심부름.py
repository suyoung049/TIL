order = ["cafelatte", "americanoice", "hotcafelatte", "anything"]

def solution(order):
    answer = 0
    for coffee in order:
        word = coffee[:3]
        if coffee == "anything":
            answer += 4500
        else:
            if word == "caf":
                answer += 5000
            elif word == "ame":
                answer += 4500
            
            elif (word == "hot" or word == "ice"):
                last = coffee[3:]
                if last == "cafelatte":
                    answer += 5000
                else:
                    answer += 4500
        
    print(answer)
    return answer

solution(order)

