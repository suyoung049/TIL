r = 5
s = 2
p = 0

rsp = "205"
answer = []

rsp = list(map(int, rsp.strip()))

for i in rsp:
    if i == 2:
        answer.append(0)
    
    elif i == 0:
        answer.append(5)
    
    elif i == 5:
        answer.append(2)

result = ''

for i in answer:
    result += str(i)

print(result)

