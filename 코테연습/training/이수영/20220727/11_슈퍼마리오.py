m = []  # [10, 20, 30, ...... 100]
score = 0
for i in range(10):  # 10개 짜리
    m.append(int(input()))
for j in m:
    score += j
    if score >= 100:
        if score - 100 > 100 - (score - j): # 
            score -= j
        break
print(score)


