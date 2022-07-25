word = input()

for idx in range(len(word)): # range(len(word)) => range(6) => 0 ~ 5
    if word[idx] == 'a':
        n = idx
        break
    else:
        n = -1
print(n)
    
        
    