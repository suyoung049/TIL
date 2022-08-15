for char in 'apple':
    if char == 'a':
        print('')
    else:
        print((char), end = '')

# 강사님 풀이
word = 'apple'  
result = ''                     # continue로 하는 방법도 있다.
for char in 'apple':
    if char != 'a':
        result = result + char
print(result)
        
        
       
    
