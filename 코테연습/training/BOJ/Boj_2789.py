word = ('C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E')
text = input()

for chr in word:
    text = text.replace(chr, '')
print(text)
   