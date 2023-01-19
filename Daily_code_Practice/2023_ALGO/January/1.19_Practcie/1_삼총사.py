from itertools import combinations

number = [-3, -2, -1, 0, 1, 2, 3]

answer = 0

for friend in combinations(number, 3):
    if sum(friend) == 0:
        answer += 1

print(answer)