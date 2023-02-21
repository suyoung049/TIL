from itertools import combinations_with_replacement # 내림차순으로 작은수를 많이 쏜 경우 부터 정렬

n = 5
info = [2,1,1,1,0,0,0,0,0,0,0] # 어피치
result = [-1]
max_gap = -1

for combi in combinations_with_replacement(range(11), n): # 중복 가능 조합 정렬
    

    info_2 = [0] * 11 # 라이언

    for i in combi:
        info_2[10-i] += 1

    apeach, lion = 0, 0

    for idx in range(11):

        if info[idx] == info_2[idx] == 0:
            continue

        elif info[idx] >= info_2[idx]:
            apeach += 10 - idx

        else:
            lion += 10 -idx
    
    if lion > apeach:
        gap = lion - apeach
        if gap > max_gap:
            max_gap = gap
            result = info_2

print(result)


