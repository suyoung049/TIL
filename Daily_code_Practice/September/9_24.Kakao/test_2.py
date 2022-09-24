users = [[40,10000],[25,10000]]
emoticons = [7000, 9000]

discount = [10, 20, 30, 40]


                
# 경우의 수 [둘다 할인 7000원만 할인, 9000원만 할인  3가지]

user = [[40,10000]]
result = []

for emo in emoticons:
    for dis in discount:
        if user[0][0] <= dis:
            prise = emo - (emo*(dis/100))
            result.append(prise)
