food = [1,7,1,2]

result =''

for i in range(1, len(food)):
    n = food[i]//2

    result += str(i) * n


answer =''

answer = result + '0' + result[::-1]

print(answer)
    
    