import re
from itertools import permutations

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["*rodo", "*rodo", "******"]

n = len(banned_id)
answer = set()

new_banned_id = []
for i in banned_id:
    new_i = i.replace("*", ".")
    new_banned_id.append(new_i)

for j in permutations(user_id, n):
    list_j = list(j)
    check = True

    for k in range(n):
     
        if re.match(new_banned_id[k], list_j[k]) and len(list_j[k]) == len(new_banned_id[k]):
            continue
        else:
            check = False
    
    if check == True:
        list_j.sort()
        if tuple(list_j) not in answer:
            answer.add(tuple(list_j))
print(answer)
