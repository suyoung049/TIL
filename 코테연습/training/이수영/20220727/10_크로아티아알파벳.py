alphabet = ['c=', 'c', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
text = input()


for word in alphabet:
    text = text.replace(word, '@')
print(len(text))
    