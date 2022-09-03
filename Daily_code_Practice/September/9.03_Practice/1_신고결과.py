id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

declaration = [0]*len(id_list)


report = set(report)

dict_ = {}
check = {}

for name in report:
    a, b = name.split()
    
    if b in check:
        check[b] += 1
    else:
        check[b] = 1

    if a not in dict_:
        dict_[a] = [b]

    else:
        if b not in dict_[a]:
            dict_[a] += [b]
print(check)
print(dict_)
for id, num_ in check.items():
    if num_ >= k:
        for id_1,id_2 in dict_.items():
            if id in id_2:
                declaration[id_list.index(id_1)] += 1

print(declaration)
