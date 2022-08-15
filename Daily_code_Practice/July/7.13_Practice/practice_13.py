chars = input() #range(len(chars))
for idx in range(len(chars)):
    print(idx)
    print(chars[-1-idx], end ='')

# 강사님 풀이
word = 'apple'
result = ''
for char in word:
    result = char + result
print(result)

print(word[::-1])