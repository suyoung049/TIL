from itertools import permutations

k = 80

dungeons = [[80,20],[50,40],[30,10]]


temp = [i for i in range(len(dungeons))]
order = list(permutations(temp, len(dungeons)))
cnt = 0

for i in order:
    i_k = k
    i_cnt = 0
    for j in i:
        if i_k >= dungeons[j][0]:
            i_k -= dungeons[j][1]
            i_cnt += 1

        else:
            break
    cnt = max(i_cnt, cnt)


print(order)
print(cnt)
