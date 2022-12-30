phone_number = "027778888"
answer = ''

len_ = len(phone_number)

for i in range(len_):
    if i < len_-4:
        answer += '*'
    
    else:
        answer += phone_number[i]

print(answer)