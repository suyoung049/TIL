
ingredient =[2, 1, 1, 2, 3, 1, 2, 3, 1]

answer = 0
i = 0

while True:
    if i < len(ingredient) -3:
        if ingredient[i] == 1:
            if ingredient[i:i+4] == [1, 2, 3, 1]:
                del ingredient[i:i+4]
                i = 0

                answer += 1
                continue
            else:
                i += 1
        
        else:
            i += 1
    
    else:
        break

print(answer)
