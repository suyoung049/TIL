word = 'banana'

result = {} # 딕셔너리
for char in word:
    # 딕셔너리에 키가 없으면 ?
    if not char in result:
        result[char] = 1
    else:
        result[char] = result[char] + 1
print(result)

word = 'HappyHacking'

result = {}
for char in word:
    result[char] = result.get(char, 0) + 1
    # result['a'] 없으면 keyError
    # result.get('a') 기본값이 None
    # result.get('a', 0) 기본값이 0
print(result)

for key in result:
    print(key, result[key])

for key, value in result.items():  # .items() : 딕셔너리의 모든 키-값의 상을 담은 뷰 반환
        f.write(f'{key}, {value}\n') 