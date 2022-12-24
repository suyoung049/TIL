from collections import Counter
k = 6
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
answer = 0
sum = 0
tan = Counter(tangerine).most_common()


for t in tan:
    sum += t[1]
    answer += 1
    if sum >= k:
        print(answer)
        break


count = 0

box = {}

for tan in tangerine:
    if tan in box:
        box[tan] += 1
    
    else:
        box[tan] = 1

while True:
    max = 0
    for key in box:
        if(box[key]) > max:
            max = box[key]
            maxi = key
        
    del box[maxi]
    if k > max:
        k = k - max
        count += 1

    else:
        count += 1
        break

print(count)




    