text = list(input())


idx_list = [0]

for i in range(len(text)):
    if text[i] == '-':
        idx_list.append(i+1)
idx = list(map(int, idx_list))

for num_ in idx:
    print(text[num_], end = '')

    

