my_string = "I love you"
num1 = 3
num2 = 6
answer = ''


for i in range(len(my_string)):
    if i == num1:
        answer += my_string[num2]
    
    elif i == num2:
        answer += my_string[num1]

    else:
        answer += my_string[i]


print(answer)