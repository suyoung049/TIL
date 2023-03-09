from itertools import combinations

numbers = [5,0,2,7]
result = [2,3,4,5,6,7] 
answer = []

for i in combinations(numbers, 2):
    if sum(i) not in answer:
        answer.append(sum(i))

answer.sort()
print(answer)



