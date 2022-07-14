word = input()

for idx in range(len(word)):
     if word[idx] == 'a':
          print(idx, end ='')


word = 'banana'
result = []
for idx in range(len(word)):
     if word[idx] == 'a':
          result.append(idx)
print(result)