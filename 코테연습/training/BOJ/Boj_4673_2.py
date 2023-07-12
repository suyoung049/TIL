na_num = set(range(1, 101))
de_sum = set()

for i in range(1, 101):
    for j in str(i):
        i += int(j)
    de_sum.add(i)
self_num = sorted(na_num - de_sum)

for i in self_num:
    print(i)
