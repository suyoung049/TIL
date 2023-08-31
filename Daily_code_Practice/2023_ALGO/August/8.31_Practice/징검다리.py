stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3

result = 0
i = 0
while True:
    check = True
    if i > len(stones) -1:
        result += 1
    
        i = 0

    if stones[i] != 0:
        stones[i] -= 1
        i += 1
    
    elif stones[i] == 0:
        for j in range(1, k):
            if i + j > len(stones) -1:
                i = i + j
                check = False
                break
            if stones[i + j] != 0:
                i = i + j
                check = False
                break
        if check == True:
            break
print(result)    
    
            
  

    
