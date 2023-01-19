N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
result = []

score = {}

for i in range(1, N+1):
    sucess = 0
    for st in stages:
        if i <= st:
            sucess += 1
    
    if sucess == 0:
        per = 0

    else:
        per = stages.count(i)/sucess

    score[i] = per

score = dict(sorted(score.items(), key = lambda x : (-x[1], x[0]) ))

for i in score:
    result.append(i)

print(result)

 