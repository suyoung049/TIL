from itertools import combinations,permutations
d = [2,2,3,3]
budget = 10

result = 0

d = sorted(d)
sum_ = 0

for num_ in d:
    sum_ += num_
    if sum_ <= budget:
        result += 1

print(result)


