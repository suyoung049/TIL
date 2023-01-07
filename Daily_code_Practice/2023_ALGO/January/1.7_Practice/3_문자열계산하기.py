my_string = "3 + 4"

num = my_string.split(' ')


stack = []

for i in num:
    if i != '+' and i != '-':
        stack.append(int(i))

    else:
        stack.append(i)

answer = stack[0]

for i in range(1, len(stack)):
    if stack[i] == '+':
        answer += stack[i+1]
    
    if stack[i] == '-':
        answer -= stack[i+1]

print(answer)

