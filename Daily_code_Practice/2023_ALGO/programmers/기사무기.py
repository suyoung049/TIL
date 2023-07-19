number = 10
limit = 3
power = 2
weapon = []


for i in range(1, number+1):
    data = set()

    for j in range(1, int(i**(1/2)) + 1):
        if i % j == 0:
            data.add(j)
            data.add(i//j)
    
    if len(data) > 0:
        weapon.append(len(data))

answer = 0
for sowrd in weapon:
    if sowrd <= limit:
        answer += sowrd
    else:
        answer += power

print(answer)



    

