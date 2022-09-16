import itertools
# text = ['a','b','c','d','e']
# qw = []

# for j in itertools.combinations(text, 5):
#         qw.append(j)
# print(qw)

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
cource = [2,3,4]
result = []
answer = []


for i in cource:
    for j in orders:

        for k in itertools.combinations(j, i):
            result.append(''.join(k))

for j in orders:
    if result.count(j) >= 2:
        answer.append(j)
answer.sort()

print(answer)
        


         
