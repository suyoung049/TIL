
n = 5
lost = [2, 4]
reserve = [1, 3, 5]

set_reserve = set(reserve) - set(lost)
set_lost = set(lost) - set(reserve)

for i in set_reserve:
    if i - 1 in set_lost:
        set_lost.remove(i-1)
    elif i + 1 in set_lost:
        set_lost.remove(i+1)

print(n - len(set_lost))