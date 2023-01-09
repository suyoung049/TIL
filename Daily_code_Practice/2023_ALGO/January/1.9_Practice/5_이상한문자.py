s = "try hello world"

answer = ''

chr_ = s.split(' ')

for i in range(len(chr_)):
    t = len(chr_[i])
    text =''
    for j in range(t):
        if j % 2 == 0:
            y = chr_[i][j].upper()
            text += y

        else:
            y = chr_[i][j].lower()
            text += y
    
    if i == 0:
        answer = answer + text
    
    else:
        answer = answer + ' ' + text

print(answer)
    
