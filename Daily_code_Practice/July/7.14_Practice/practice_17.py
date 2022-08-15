word = input()
word = list(word)
a = 0
for idx in word:
    a = ord(idx)
    print(chr(a-32), end ='')

word = 'banana'
result =''
for char in word:
    num = ord(char)
    num = num - 32
    result += chr(num)
print(result)


