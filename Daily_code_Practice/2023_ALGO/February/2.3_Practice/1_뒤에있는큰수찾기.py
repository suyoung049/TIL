numbers = [2, 3, 3, 5]
result = []

for y in range(len(numbers)):
    for j in range(y+1, len(numbers)):
        if numbers[y] < numbers[j]:
            result.append(numbers[j])
            break
    else:
        result.append(-1)

            
    
