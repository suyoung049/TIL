lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]


con = 0

for i in lottos:
    if i in win_nums:
        con += 1

if con == 0:
    min_score = 6

else:
    min_score = 7 - con



zero = lottos.count(0)

if (con + zero) == 0:
    max_score = 6

else:
    max_score = 7 - (con + zero)

result = [max_score, min_score]

print(result)


