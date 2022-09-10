lotto = [45, 4, 35, 20, 3, 9]
win_numbers = 	[20, 9, 3, 45, 4, 35]


count_ = 0

for num_ in lotto:
    if num_ in win_numbers:
        count_ += 1

random = lotto.count(0)

max_ = count_ + random

result = [max_,count_]
answer = []

for i in range(2):
    if result[i] > 1:
        answer.append(7-result[i])
    else:
        answer.append(6)

print(answer)
