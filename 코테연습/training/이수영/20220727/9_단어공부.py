text = input().upper()

words = list(set(text))
count_ = []

for x in words:
    cnt = text.count(x)
    count_.append(cnt)
if count_.count(max(count_)) > 1:
    print('?')
else:
    max_index = (count_.index(max(count_)))
    print(words[max_index])