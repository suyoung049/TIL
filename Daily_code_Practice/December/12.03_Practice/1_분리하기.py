s = "aaabbaccccabba"
stack =[]

x_count = 0
y_count = 0
count = 0


for i in range(len(s)):
    stack.append(s[i])

    if stack[0] == s[i]:
        x_count += 1

    else:
        y_count += 1
    
    if x_count == y_count:
        count += 1
        x_count = 0
        y_count = 0
        stack = []
    
    else:
        if i == len(s) -1 :
            count += 1

print(count)



    


