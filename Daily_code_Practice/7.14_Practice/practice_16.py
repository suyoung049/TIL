word = input()
count = 0
for chr in word:
    if chr in ['a', 'e', 'o', 'u']:
        count += 1

print(count)