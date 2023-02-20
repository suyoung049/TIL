import math
fees = [1, 461, 1, 10]
records = ["00:00 1234 IN"]
car = {}
park_time = {}
result = []

for record in records:
    record = record.split()
    time = record[0].split(':')
    time = 60 * int(time[0]) + int(time[1])
    if record[2] == 'IN':
        car[record[1]] = time
    elif record[2] == 'OUT':
        car[record[1]] = time - car[record[1]]
        park = car.pop(record[1])
        if record[1] not in park_time:
            park_time[record[1]] = park
        else:
            park_time[record[1]] = park_time[record[1]] + park

if car:
    for i in car:
        park = 1439 - car[i]
        if i not in park_time:
            park_time[i] = park
        else:
            park_time[i] = park_time[i] + park

for i in park_time:
    if park_time[i] <= fees[0]:
        park_time[i] = fees[1]
    else:
        park_time[i] = fees[1] + math.ceil((park_time[i]-fees[0])/fees[2]) * fees[3] 


park_time = sorted(park_time.items(), key=lambda x: x[0])

for i in park_time:
    result.append(i[1])

print(result)