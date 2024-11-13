import sys
sys.stdin = open('1_input.txt', 'r')

n = int(input())

str_li = []
str_dict = dict()

# 단어들을 입력받아 리스트에 저장
for _ in range(n):
    input_str = input()
    str_li.append(input_str)

for word in str_li:
    temp = ""
    length = len(word)

    for i in range(length):
        temp += word[i]

        if temp in str_dict:
            str_dict[temp] += 1
        else:
            str_dict[temp] = 1

prefix = ""
max_length = 0
for key in str_dict:
    if len(key) > max_length and str_dict[key] > 1:
        prefix = key
        max_length = len(key)

cnt = 0
for word in str_li:
    if word[:max_length] == prefix:
        cnt += 1
        print(word)
    if cnt == 2:
        break



