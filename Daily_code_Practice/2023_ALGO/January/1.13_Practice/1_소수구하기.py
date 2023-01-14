from itertools import combinations

nums = [1,2,7,6,4]
result = 0

re_nums = []

for i in combinations(nums, 3):
    re_nums.append(sum(i))


for j in re_nums:
    for k in range(2, int(j**0.5)+1):
        if j % k == 0:
            break
    else:
        result += 1

print(result)
    

