# 조합을 뽑아야 할때 중복값이 필요하면 백트래킹 고려 
users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]
answer = [0, 0]
temp_answer = [0, 0]
data = [10, 20, 30, 40]
discount = []


def dfs(tmp, d):
    if d == len(tmp):
        discount.append(tmp[:])
        return

    else:
        for i in data:
            tmp[d] += i
            dfs(tmp, d+1)
            tmp[d] -= i


dfs([0]*len(emoticons), 0)

for persent in discount:
    price = 0
    temp_answer[0] = 0

    for user in users:

        for i in range(len(emoticons)):
            if persent[i] >= user[0]:
                temp_answer[1] += (emoticons[i] *((100-persent[i])/100))
               
            
        if temp_answer[1] >= user[1]:
            temp_answer[1] = 0
            temp_answer[0] += 1
        
        price += temp_answer[1]
        temp_answer[1] = 0 
            
    if temp_answer[0] < answer[0]:
        continue

    if temp_answer[0] > answer[0]:
        answer[0] = temp_answer[0]
        answer[1] = price
      
    
    elif price > answer[1]:
        answer[1] = int(price)
        

print(answer)