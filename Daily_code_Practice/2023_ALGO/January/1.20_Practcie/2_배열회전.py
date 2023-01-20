numbers = [4, 455, 6, 4, -1, 45, 6]
direction = 'left'
n = len(numbers)
stack = [0] * n


for i in range(n):
    if direction == 'right':
        if i == n-1:
            stack[0] = numbers[n-1]

        else:
            stack[i+1] = numbers[i]       
    
    elif direction == 'left':
        if i == 0:
            stack[n-1] = numbers[0]
        
        else:
            stack[i-1] = numbers[i]
        
print(stack)
