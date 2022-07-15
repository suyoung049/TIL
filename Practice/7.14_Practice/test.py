word = 'banana'

result = {} # 딕셔너리
for char in word:
    # 딕셔너리에 키가 없으면 ?
    if not char in result:
        result[char] = 1
    else:
        result[char] = result[char] + 1
print(result)